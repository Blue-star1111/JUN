<template>
  <div id="HomeView" class="contents-view">
    <div>
      <v-card
        class="mx-auto"
        min-width="100%"
        height="200px"
        :img="require('../assets/images/main2.jpg')"
      >
        <div class="header">
          <v-card-title>
            <h1>
              SHE management system
            </h1>
          </v-card-title>
          <v-card-text>
            <p>It is an information system for integrated management of information in the fields of safety, health, and energy that are distributed within the company.</p>
          </v-card-text>
        </div>
      </v-card>
    </div>
    <div>
      <br><br>
      <v-flex xs12>
        <v-row>
          <v-col>
            <v-card
              class="grow" 
              color="#ECEFF1" 
              width="300px"
            >
              <v-card-actions class="justify-center">
                <v-img
                  class="white--text align-end"
                  width="250px"
                  height="250px"
                  src="../assets/images/safety_main.jpg"
                />
              </v-card-actions>
              <v-card-title>
                <h2 class="pa-1">SAFETY</h2>
              </v-card-title>
              <v-divider></v-divider>
              <br>
              <router-link to="/main/safety"><h3>Safety Monitoring</h3></router-link>
              <br>
            </v-card>
          </v-col>
          <v-col>
            <v-card class="grow" color="#ECEFF1" width="300px">
              <v-card-actions class="justify-center">
                <v-img
                  width="250px"
                  height="250px"
                  src="../assets/images/health_main.jpg"
                />
              </v-card-actions>
              <v-card-title>
                <h2 class="pa-1">HEALTH</h2>
              </v-card-title>
              <v-divider></v-divider>
              <br>
              <router-link to="/main/health"><h3>Self-Check</h3> </router-link> 
              <br>
            </v-card>
          </v-col>
          <v-col>
            <v-card class="grow" color="#ECEFF1" width="300px">
              <v-card-actions class="justify-center">
                <v-img
                  width="250px"
                  height="250px"
                  class="white--text align-end"
                  src="../assets/images/environ_main.jpg"
                />
              </v-card-actions>
              <v-card-title>
                <h2 class="pa-1">ENERGY</h2>
              </v-card-title>
              <v-divider></v-divider>
              <br>
              <router-link to="/main/energy"><h3>Dashboard</h3></router-link>
              <br>
            </v-card>
          </v-col>
        </v-row>
      </v-flex>
    </div>
  </div>
</template>

<script>
  export default {
    data() {
      return {

      }
    }
  }
</script>

<style>
.header{
  width: 51%;
}
h1{
  margin-top: 5%;
  margin-left: 10%;
}
p{
  margin-top: 3%;
  margin-left: 10%;
}
a {
  text-align: center;
  text-decoration: none;
  color: navy;
}
.grow {
  transition: all .2s ease-in-out;
  margin-left: 10%;
}
.grow:hover { 
  transform: scale(1.1); 
}
.pa-1 {
  margin-left: 28%;
}
</style>