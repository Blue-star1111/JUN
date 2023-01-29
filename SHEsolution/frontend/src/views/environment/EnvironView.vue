<template>
  <div id="DashboardView" class="contents-view">
    <v-container class="container-view">
      <v-flex>
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
                src="../../assets/images/energy.jpg"
              >
                <v-card-title >
                  <h1>Electric Power Dashboard</h1>
                </v-card-title>
              </v-img>
            </v-card>
          </v-col>
        </v-row>
      </v-flex>
      <br>
      <v-flex>
        <v-card style="padding: 0 30px 0 30px;">
          <v-row>
            <v-col>
              <h2><v-icon>mdi-monitor</v-icon>&nbsp;Real-Time Monitoring</h2>
            </v-col>
          </v-row>
          <v-row>
            <v-col>
              <vue-friendly-iframe :src=srcList[0] className="grafana-view"></vue-friendly-iframe>
            </v-col>
            <v-col>
              <vue-friendly-iframe :src=srcList[1] className="grafana-view"></vue-friendly-iframe>
            </v-col>
            <v-col>
              <vue-friendly-iframe :src=srcList[2] className="grafana-view"></vue-friendly-iframe>
            </v-col>
          </v-row>
          <v-row>
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
                  v-on:change="fetchGrafanaURL"
                ></v-date-picker>
              </v-menu>
            </v-col>
          </v-row>
          <v-row>
            <v-col>
              
              <h2><v-icon>mdi-monitor</v-icon>&nbsp;Historical Dashboard</h2>
            </v-col>
          </v-row>
          <v-row>
            <v-col>
              <vue-friendly-iframe :src=srcList[3] className="grafana-view"></vue-friendly-iframe>
            </v-col>
            <v-col>
              <vue-friendly-iframe :src=srcList[4] className="grafana-view"></vue-friendly-iframe>
            </v-col>
          </v-row>
        </v-card>
      </v-flex>
      <v-row><br><br></v-row>
    </v-container>
  </div>
</template>

<script>
import Vue from 'vue';
import VueFriendlyIframe from 'vue-friendly-iframe';

import { grafanaURL } from '@/utils/grafana.js';
// , fetchUnixTimestamp

Vue.use(VueFriendlyIframe);

export default {
  name: 'DashboardView',

  components: {
    //
  },

  data: () => ({
    date: (new Date(Date.now() - (new Date()).getTimezoneOffset() * 60000)).toISOString().substr(0, 10),
    menu: false,
    srcList: [],
    panelIds: [6, 8, 10, 4, 2]
  }),
  created() {
    this.fetchGrafanaURL()
  },
  methods: {
    fetchGrafanaURL() {
      for (let i=0; i<this.panelIds.length; i+=1){
        this.updateSrc(i, this.panelIds[i]);
      }
    },
    updateSrc(idx, panelId) {
      this.$set(this.srcList, idx, grafanaURL + "&panelId=" + panelId);
      // + "&from=" + fetchUnixTimestamp(this.date)[0] + "&to=" + fetchUnixTimestamp(this.date)[1]
    },
  },
};
</script>

<style scoped>
h1{
  margin-top: 5px;
}
h2{
  margin-left: 20px;
  font-weight: 400;
}
</style>