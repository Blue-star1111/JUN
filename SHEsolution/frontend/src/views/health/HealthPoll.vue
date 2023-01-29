<template>
  <div id="CheckListView" class="contents-view">
    <v-container class="container-view">
      <v-row>
        <v-col>    
          <v-card
            class="mx-auto"
            min-width="100%"
          >
            <v-img
              class="white--text align-end"
              width=auto
              height="100px"
              src="../../assets/images/health.jpg"
            >
              <v-card-title>
                <h1>
                  Safety&Health Self-checklist
                </h1>
              </v-card-title>
            </v-img>
          </v-card>
        </v-col>
      </v-row>
      <v-row>
        <v-card class="history" v-for="(item,index) in history" :key="index" v-show="is_hidden">
          <v-list-item>
            <v-list-item-content>
              <v-list-item-title>체크리스트 : {{ item.title }}</v-list-item-title>
              <v-list-item-subtitle>작성일 : {{ item.date }}</v-list-item-subtitle>
            </v-list-item-content>
            <v-btn icon id="no-background-hover">
              <span>
                <v-icon size="large" @click="updateList(); hidden=!hidden">mdi-lead-pencil</v-icon>
              </span>
            </v-btn>
          </v-list-item>
        </v-card>
        <v-card class="list" v-show="hidden"> 
          <v-row>
            <!-- Date Picker -->
            <v-col
              cols="12"
              sm="6"
              md="4"
            >
              <v-menu
                v-model="menu"
                :close-on-content-click="false"
                :nudge-right="40"
                transition="scale-transition"
                offset-y
                min-width="auto"
              >
                <template v-slot:activator="{ on, attrs }">
                  <v-text-field
                    v-model="date"
                    label="search date"
                    prepend-icon="mdi-calendar"
                    readonly
                    v-bind="attrs"
                    v-on="on"
                  ></v-text-field>
                </template>
                <v-date-picker
                  v-model="date"
                  @input="menu = false"
                  readonly
                ></v-date-picker>
              </v-menu>
            </v-col>
            <!-- select -->
            <v-col
              class="d-flex"
              cols="12"
              sm="6"
            >
              <v-select
                :items="checklist"
                label="search List"
                item-text="title.title"
                item-value="title.id"
                v-model="TitleFilterValue"
              ></v-select>
            </v-col>
            <!-- button -->
            <v-col>
              <v-btn
                class="save"
                color="primary"
                @click="reset()"
              >
                reset
              </v-btn>
              <v-btn
                class="save"
                color="primary"
                @click="saveList();"
              >
                save
              </v-btn>
            </v-col>
          </v-row>
          <v-row>
            <v-col> 
              <v-data-table
              :headers="headers"
              :items="checklist"
              class="elevation-1"
              item-key="question_text"
              :footer-props="{ disablePagination : true, disableItemsPerPage : true }"
              disable-pagination
              hide-default-footer
              >
                  <template
                    v-slot:body="{ items }"
                  >
                    <tbody>
                      <tr
                        v-for="(item, index) in items"
                        :key="index"
                      >
                        <td>{{ item.question_text }}</td>
                        <td>
                          <v-radio-group
                            class="small-radio"
                            v-model="item.answer"
                            row
                          >
                            <v-radio
                              label="예"
                              v-bind:value="true"
                              color="success"
                            ></v-radio>
                            <v-radio
                              label="아니오"
                              v-bind:value="false"
                              color="red darken-3"
                            ></v-radio>
                          </v-radio-group>
                        </td>
                        <td>
                          <v-text-field
                            v-model="item.bigo"
                            color="purple darken-2"
                          ></v-text-field>
                        </td>
                      </tr>
                    </tbody>
                  </template>
              </v-data-table>
            </v-col>
          </v-row>
        </v-card>
      </v-row> 
    </v-container>
  </div>
</template>


<script>
import axios from 'axios'

  export default {
    data () {
      return {
        date: (new Date(Date.now() - (new Date()).getTimezoneOffset() * 60000)).toISOString().substr(0, 10),
        menu: false,
        checklist: [],
        history: [],
        hidden : true,
        is_hidden : true,

        // Call Backend API(using Axios) 
        TitleFilterValue: 2,
      }
    },
    computed: {
      headers() {
        return [
          { text: '항목',
            value: 'title.id',
            width: '55%',
            filter: this.TitleFilter,
          },
          { text: '점검', value: 'answer', width: '20%' },
          { text: '비고', value: 'bigo', width: '35%' },
        ]
      },
    },
    methods: {
      // Search
      TitleFilter(id) {
        // console.log(this.TitleFilterValue);
        if (!this.TitleFilterValue) {
          return true;
        }
        return id === this.TitleFilterValue;
      },
      
      // Save
      saveList() {
        for (let i=0; i<this.checklist.length; i+=1){
          if (this.checklist[i].title.id == this.TitleFilterValue){
            if (this.checklist[i].answer == null){
              // console.log(this.checklist[i].answer);
              alert("아직 체크되지 않은 문장이 있습니다.");
            }
            // alert("저장하시겠습니까?")
            const inputData = {
              title: {id: this.checklist[i].title.id, title: this.checklist[i].title},
              question_text: this.checklist[i].question_text,
              answer: this.checklist[i].answer,
              bigo: this.checklist[i].bigo
            };
            

            axios.put("/checklist/"+this.checklist[i].id+"/", inputData)
            .catch((err)=>{
              console.log(err)
            });
            // const listTitle = this.checklist[i].title;
            // const listDate = this.date;
            // const listHistory = [];
            // const listItem = {
            //   title: listTitle,
            //   date: listDate,
            // };
            // listHistory.push(listItem);
            // axios.post('/history/')
            // .then((res) => {
            //   this.$emit('saved')
            //   this.history = res.data; 
            // })
            // .catch((err) => {
            //   console.log(err)
            // })  
          }
        }
        
        // this.hidden = !this.hidden
        // this.is_hidden = !this.is_hidden
      },
      reset() {
        for (let i=0; i<this.checklist.length; i+=1){
          if (this.checklist[i].title.id == this.TitleFilterValue){
            this.checklist[i].answer = null
          }
        }
      },
      // updateList() {

      // },
      // Call INSERT Backend API(using Axios) 
      getCheckList() {
        axios.get("/checklist/")
        .then((res)=>{
          console.log(res)
          this.checklist = res.data;
        }).catch((err)=>{
          console.log(err);
        });
      },
      // getHistory() {
      //   axios.get("/history/")
      //   .then((res)=>{
      //     console.log(res)
      //     this.history = res.data;
      //   }).catch((err)=>{
      //     console.log(err);
      //   });
      // }
    },
    created: function() {
      this.getCheckList();
      // this.getHistory();
    }
  }
</script>

<style scoped>
h1{
  margin-top: 5px;
}
.save{
  margin-top: 10px;
  margin-left: 25%;
}
.list{
  width: 98%;
  margin: 20px 20px 30px 20px;
  padding-left: 10px;
}
</style>