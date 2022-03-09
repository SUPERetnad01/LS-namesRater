<template>
  <v-app>
    <v-main>
      <v-row class="justify-center">
        <v-col cols=6 md=6 sm=12>
          <h1 v-if="response" class="text-h1">{{response.message}}</h1>
          <h2 v-if="response" class="text-h2">{{response.rating}}</h2>
          
          <v-container class="pt-12">
            <v-text-field v-model="formData.ign" label="Summoner name" variant="contained" @keyup.enter="getRating()"/>
            <v-row align="center" justify="end">
              <v-btn color='red' class="mr-4" style="color:white !important;" @click="getRating()">Rating!</v-btn>
            </v-row>
          </v-container>
        </v-col>
      </v-row>
    </v-main>
  </v-app>
</template>

<script>
export default {
  name: 'App',

  data: () => ({
    formData: {},
    response: {}
  }),

  methods: {
    getRating() {
      this.axios.get('http://localhost:5000/predict', {params: this.formData}).then((response) => {
        console.log(response.data)
        this.response = response.data
      })
    }
  },
}
</script>
