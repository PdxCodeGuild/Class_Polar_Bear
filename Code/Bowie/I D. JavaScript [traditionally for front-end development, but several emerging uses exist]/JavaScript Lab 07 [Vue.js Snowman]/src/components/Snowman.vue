<template>
  <div class="container bg-light p-4">
    <h2>Snowman/"Bonhomme de Neige"</h2>
    <div v-if="word" class="my-4 word-container">
      <div class="word-item mx-2 d-flex justify-content-center align-items-center" v-bind:class="{'bg-dark': !item.show, 'show-letter': item.show}" v-for="(item, index) in wordArr" :key="index">
        {{item.show ? item.value : ''}}
      </div>
    </div>
    <div v-if="this.word">
      <b-button class="btn-sm m-1" v-bind:disabled="item.selected" :variant="item.selected ? 'danger' : 'primary'"
          v-for="item in letters" :key="item.value" @click="() => {item.selected = true; find(item.value)}">{{item.value}}</b-button>
      <Output v-bind:count="count" />
    </div>
  </div>
</template>

<script>
import Output from './Output.vue'

export default {
  name: 'Snowman',
  components: {
    Output
  },
  props: {
    forceRerender: Function
  },
  data: () => ({
    word: null,
    wordArr: null,
    letters: [],
    count: 10,
  }),
  methods: {
    watchCount: function() {
      if(!this.count) {
        alert('You Lose');
        this.forceRerender();
      }
      let lettersLeft = this.wordArr.filter(el => !el.show);
      if(!lettersLeft.length) {
        alert('Congratulations!');
        this.forceRerender();
      }
    },
    find: function(value) {
      value = value.toLowerCase();
      let isFound = false;
      this.wordArr.forEach(el => {
        if(el.value === value) {
          el.show = true;
          isFound = true;
        }
      })
      if(!isFound) {
        this.count--;
      }
      setTimeout(this.watchCount, 500);
    }
  },
  mounted() {
    this.axios.get('https://random-word-api.herokuapp.com/word/?swear=0').then(res => {
      if(res.data?.length) {
        this.word = res.data[0];
        this.wordArr = this.word.split('').map(el => ({value: el, show: false}));
      }
    });
    const alpha = Array.from(Array(26)).map((e, i) => i + 65);
    const alphabet = alpha.map(x => String.fromCharCode(x));
    this.letters = alphabet.map(letter => ({value: letter, selected: false}));
  }
}
</script>

<style scoped>
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
.word-item {
  height: 3rem;
  width: 2rem;
}
.word-container {
  display: flex;
}
.show-letter {
  border: 2px solid #28A745;
  font-size: 3rem
}
</style>
