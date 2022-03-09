<script setup>

</script>

<template>
    <div>
      <form action="http://localhost:5000/predict">
          <label for="ign" class="form-label">Summoner name</label>
          <input class="form-control form-control-lg" type="text" id="ign" placeholder="Your summoner name here" name="ign">

          <!-- <input type="submit" value="Submit"> -->
          <div class="d-flex justify-content-end my-4">
            <button type="submit" class="btn btn-primary">Request rating</button>
          </div>
            <button @click="getRating()">Request rating</button>

        </form>
        <h2 class="display-1 text-center">{{ message }}</h2>
        <br>
        <h2 class="display-2 text-center">{{ rating }}</h2>
  </div>
</template>

