<template>
    <div id="MenuView">
        <v-card
        height="100%"
        width="256"
        class="mx-auto;"
        style="position: fixed;"
        >
            <v-navigation-drawer class="drawer" style="background-color:beige" permanent>
                <v-list-item>
                    <v-list-item-content>
                        <a @click="makeActive('home')" style="text-decoration:none;">
                            <v-list-item-title>
                                <h3>SHE Portal</h3>
                            </v-list-item-title>
                            <v-list-item-subtitle>
                                <p>Safefy, Health, Energy</p>
                            </v-list-item-subtitle>
                        </a>
                    </v-list-item-content>
                </v-list-item>
                <br>
                <v-divider></v-divider>
                <br>
                <v-list
                dense
                nav
                >
                <v-list-item
                    class="pages"
                    v-for="item in items"
                    :key="item.title"
                    link
                    
                >
                    <v-list-item-icon>
                    <v-icon large>{{ item.icon }}</v-icon>
                    </v-list-item-icon>
        
                    <v-list-item-content>
                    <a @click="makeActive(item.active)" style="text-decoration:none;">
                        <v-list-item-title><h4>{{ item.title }}</h4></v-list-item-title>
                    </a>
                    </v-list-item-content>
                </v-list-item>
                </v-list>
            </v-navigation-drawer>
        </v-card>
    </div>
  </template>

<script>
export default {
    data () {
        return {
            items: [
                { title: 'Home', icon: 'mdi-home', active: 'home'  },
                { title: 'Safety Monitoring', icon: 'mdi-image', active: 'safety' },
                { title: 'Self-Check', icon: 'mdi-pencil', active: 'health' },
                { title: 'Dashboard', icon: 'mdi-view-dashboard', active: 'energy' },
            ],
            right: null,
        }
    },
    methods: {
        makeActive(item) {
            this.$router.push({path: `/main/${item}`})
            .catch((error) => {if (error.name !== 'NavigationDuplicated') throw error});
        },
    }

}
</script>

<style scoped>
.drawer{
    padding-top: 15px;
}
h3 {
    text-align: center;
    font-size: 22px;
}
p{  
    margin-top: 10px;
    margin-left: -2px;
    color: black;
}
a{
    text-align: center;
    font-weight: bolder;   
}
h4{
    font-size: 15px;
    color: black;
}
.pages{
    padding-top:10px;
}
</style>