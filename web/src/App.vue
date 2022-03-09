<template>
  <v-app>
    <v-main>
      <v-row class="justify-center">
        <v-col cols=6 md=6 sm=12>
          <h1 v-if="response" class="text-h1">{{response.message}} {{response.rating}}</h1>
          <v-container class="pt-12">
            <v-text-field v-model="formData.ign" label="Summoner name" variant="contained"/>
           <v-btn color='primary' class="justify-end" @click="getRating()">Rating!</v-btn>
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
