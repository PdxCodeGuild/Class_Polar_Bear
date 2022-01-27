<template>
  <div id="app">
    <UnitConverter />
  </div>
</template>

<script>
import UnitConverter from './components/UnitConverter.vue'

export default {
  name: 'App',
  components: {
    UnitConverter
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
