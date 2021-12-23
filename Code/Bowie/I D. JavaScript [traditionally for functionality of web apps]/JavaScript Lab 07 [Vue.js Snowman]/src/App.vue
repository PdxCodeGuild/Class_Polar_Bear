<template>
  <div id="app">
    <Snowman  v-if="renderComponent" v-bind:forceRerender="forceRerender" />
  </div>
</template>

<script>
import Snowman from './components/Snowman.vue'

export default {
  name: 'App',
  components: {
    Snowman
  },
  data: () => ({
    renderComponent: true
  }),
  methods: {
    forceRerender() {
      this.renderComponent = false;

      this.$nextTick(() => {
        this.renderComponent = true;
      });
    }
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
