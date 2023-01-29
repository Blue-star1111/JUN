<template>
  <div id="app" data-app>
    <router-view/>
  </div>
</template>

<script>
export default {
  name: 'App',

  components: {
    //
  },

  data: () => ({
    //
  }),
};
</script>

<style lang="scss">
  @import './assets/styles/common.scss';

  html, body {
    margin: 0;
    height: 100%;
    overflow: hidden;
  }
  #app {
    outline: none;
    -webkit-outline:none;
    background-color:#fff;
    margin: 0;
    padding: 0;
    width: 100%;
    height: 100%;
    overflow-y: auto;
  }
</style>
