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
            :items="listInput"
            label="search List"
            item-text="question_text.title.title"
            item-value="question_text.title.id"
            v-model="TitleFilterValue"
          ></v-select>
        </v-col>
        <!-- button -->
        <v-col>
          <v-btn
            class="save"
            color="primary"
            @click="setCheck()"
          >
            save
          </v-btn>
        </v-col>
      </v-row>
      <v-row>
        <v-col> 
          <v-data-table
          :headers="headers"
          :items="listInput"
          class="elevation-1"
          item-key="question_text"
          :footer-props="{ disablePagination : true, disableItemsPerPage : true }"
          :disable-pagination="true"
          hide-default-footer
          >
              <template
                v-slot:body="{ items }"
              >
                <tbody>
                  <tr
                    v-for="item in items"
                    :key="item.name"
                  >
                    <td>{{ item.question_text.question_text }}</td>
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
        Type: [],
        listInput : [],

        // Call Backend API(using Axios) 
        TitleFilterValue: 1,
      }
    },
    computed: {
      headers() {
        return [
          { text: '항목',
            value: 'question_text.title.id',
            width: '55%',
            filter: this.TitleFilter,
          },
          { text: '점검', value: 'answer', width: '15%' },
          { text: '비고', value: 'bigo', width: '40%' },
        ]
      },
    },
    methods: {
      // Search
      TitleFilter(id) {
        console.log(this.TitleFilterValue);
        if (!this.TitleFilterValue) {
          return true;
        }
        return id === this.TitleFilterValue;
      },
      
      // Save
      setCheck() {
        console.log(this.listInput)
        // inputData = []
        // const inputDate = this.date;
        // const inputType = this.TitleFilterValue;

        for (let i=0; i<this.listInput.length; i+=1){
          if (this.listInput[i].question_text.title.id == this.TitleFilterValue){
            if (this.listInput[i].answer == null){
              console.log(this.listInput[i].answer);
              alert("아직 체크되지 않은 문장이 있습니다.");
              return
            }
            // console.log(this.listInput[i].answer);
            // const inputData = {
            //   question_text : this.listInput[i].question_text.question_text,
            //   answer: this.listInput[i].answer,
            //   bigo: this.listInput[i].bigo
            // }
            // axios.post("http://127.0.0.1:8000/listinput/", inputData)
            //   .then((res) => {
            //     console.log(res);
            //   })
            //   .catch((err) => {
            //     console.log(err);
            //   });
          }
        }     
      },
      // Call INSERT Backend API(using Axios) 
      getListType() {
        axios.get("http://127.0.0.1:8000/type/")
        .then((res)=>{
          this.Type = res.data;
        }).catch((err)=>{
          console.log(err);
        });
      },
      getListInput() {
        axios.get("http://127.0.0.1:8000/listinput/")
        .then((res)=>{
          this.listInput = res.data;
          console.log(res.data)
        }).catch((err)=>{
          console.log(err);
        });
      }
    },
    created: function() {
      this.getListType();
      this.getListInput();
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
</style>