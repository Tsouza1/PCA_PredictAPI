<template>
  <v-container>
    <v-layout text-xs-center wrap>
      <v-flex>
        <!-- IMPORTANT PART! -->
        <form>

          <v-text-field v-model="title" label="Titulo" required></v-text-field>
          <v-select v-model="gender" :items="itens_g" label="Gênero" required></v-select>
          <v-select v-model="type" :items="itens_t" label="Tipo" required></v-select>

          <v-btn @click="submit">submit</v-btn>
          <v-btn @click="clear">clear</v-btn>

        </form>
        <!-- <h1 v-if="percentClass">{{ krl }}</h1> -->
        <br />
        <br />
        <h1 v-if="predictedClass">Nota prevista para o filme {{ title }} : {{ predictedClass }}</h1>
        <!-- END: IMPORTANT PART! -->
        <br/>
        <!-- <apexchart width="380" type="donut" :options="options" :series="series"></apexchart> -->
      </v-flex>
    </v-layout>
  </v-container>
</template>

<script>
import axios from "axios";
// import { serverBus } from '../main';
export default {
  name: "HelloWorld",
  data: () => ({
    predictedClass: "",
    percentClass: "",
    krl: "",
    loaded: false,
      // options: {},
      // series: [44, 55, 41, 17, 15],
    title: "",
    gender: null,
    itens_g: [
      {text: "Drama", value: 1},
      {text: "Comédia", value: 2},
      {text: "Crime", value: 3},
      {text: "Horror", value: 4},
      {text: "Ação", value: 5},
      {text: "Aventura", value: 6},
      {text: "Mistério", value: 7},
      {text: "Suspense", value: 8},
      {text: "Fantasia", value: 9},
      {text: "Romance", value: 10},
    ],
    type: null,
    itens_t: [
      {text: 'Filme', value: 1},
      {text: 'Serie', value: 2}
      ]
  }),
  methods: {
    submit() {
      
      axios.post("http://127.0.0.1:5000/predict", {
          gender: this.gender,
          type: this.type,
        })
        .then(response => {
          this.predictedClass = response.data;
        }),
      axios.post("http://127.0.0.1:5000/percent", {
          gender: this.gender,
          type: this.type,
        })
        .then(response => {
          this.percentClass = response.data;
          // this.krl = this.percentClass.split(",");
          this.krl = this.percentClass
          console.log(typeof this.krl)/* eslint-disable-line no-console */
          this.$emit('percent', this.krl)
        })
                     
    },      
    clear() {
      this.title = "";
      this.gender = "";
      this.type = "";
    },
  }
};
</script>

<style>
form {
  max-width: 500px;
  margin: 0 auto;
  margin-top: 50px;
}
button{
  margin: 10px;
}
</style>>