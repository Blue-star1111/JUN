<template>
  <div id="MainView" style="height:100%">
    <menu-view></menu-view>
    <router-view name="contents" :key="$route.fullPath"></router-view>
  </div>
</template>


<script>
import MenuView from '@/views/MenuView'

export default {
  name: 'MainView',
  components: {
    MenuView
  },
  mounted() {
    this.$router.push({name : 'home'})
        .catch( (error) => { if (error.name !== 'NavigationDuplicated') throw error});
  },
  methods: {
   //
  },
};
</script>
