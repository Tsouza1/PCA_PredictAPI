<template>
  <v-app>
    <!-- <v-toolbar app>
      <v-toolbar-title class="headline text-uppercase">
        <span class="font-weight-light">My Cool Model</span>
      </v-toolbar-title>
    </v-toolbar>-->
    <v-content>
      <HelloWorld @percent="percentP($event)"/>
      <charts :percentp="percentp"/>
    </v-content>
    
  </v-app>
</template>

<script>
import HelloWorld from "./components/HelloWorld";
import charts from "./components/charts";
export default {
  name: "App",

  components: {
    HelloWorld,
    charts
  },

  data() {
      return {
          percentp: '',
      }
  },
  methods: {
    percentP(message){
      this.percentp = message
      console.log(message)/* eslint-disable-line no-console */
    },
  }
};
</script>

<style>
#app {
  font-family: "Avenir", Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
</style>

