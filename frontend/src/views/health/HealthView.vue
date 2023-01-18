<template>
  <div id="ChecklistView" class="history-view">
    <v-container fluid>
      <v-row class="justify-center">
        <v-col>
          <v-card
            class="mx-auto"
            min-width="100%"
          >
            <v-img
              class="white--text align-end"
              cover
              height="100px"
              src="../../assets/images/dashboard.jpg"
            >
              <v-card-title >
                <h1 class="text-h3 font-weight-thin mb-4" style="color: white;">
                  Checklist History
                </h1>
              </v-card-title>
            </v-img>
          </v-card>
        </v-col>
      </v-row>
      <br><br>
      <v-row class="justify-center">
          <h2>작성한 체크리스트</h2>
        <!-- <v-col>
          <v-btn color="blue" to="/health">답변 작성하기</v-btn>
        </v-col> -->
      </v-row>
      <br><br>
      <v-row class="justify-center">
        <v-card class="checklist">
          <v-list-item style="text-align:left">
            <v-list-item-title style="font-size:18px; font-weight: bold;">
              이름: 
            </v-list-item-title><br>
          </v-list-item>
          <v-list-item style="text-align:left">
            <v-list-item-subtitle style="font-size:15px; color: black; font-weight: bold;">
              작성일:  
            </v-list-item-subtitle>
          </v-list-item>
            <br>
          <v-list-item style="float:right">
            <v-btn icon id="no-background-hover" to="/health/poll">
              <span class="group pa-2">
                <v-icon size="large">mdi-lead-pencil</v-icon>
              </span>
            </v-btn>
            <v-btn icon id="no-background-hover">
              <span class="group pa-2">
                <v-icon size="large">mdi-delete</v-icon>
              </span>
            </v-btn>
          </v-list-item>
        </v-card>
      </v-row>
    </v-container>
  </div>
</template>

<script>
// import axios from "axios"

// let url = "http://localhost:8000/checklist/"

//   export default {
//     data: () => {
//       return {

//       }
//     },
//     mounted() {
//       axios({
//         method: "GET",
//         url: url
//       })
//         .then(response => {
//           this.checkvalue = response.data;
//         })
//         .catch(response => {
//           console.log("Failed", response)
//         });
//     },
//   }
</script>



<style scoped>
h2{
  text-align: center;
}
.checklist{
  width:40%;
  height:200px;
}
</style>