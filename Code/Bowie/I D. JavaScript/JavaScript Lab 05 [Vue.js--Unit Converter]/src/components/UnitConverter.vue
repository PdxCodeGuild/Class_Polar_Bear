<template>
  <div class="container bg-light p-4">
    <h4>
      I want to convert: / Je veux converter:
    </h4>
    <b-form-input v-model="count" placeholder="Enter the number / Entrez le nombre" type="number" min="0"></b-form-input>
    <b-form-select v-model="firstItem" :options="options" class="my-3"></b-form-select>
    <h4>→</h4>
    <b-form-select v-model="secondItem" :options="options"></b-form-select>
    <div v-if="firstItem && secondItem" class="mt-3">
      <h4> ≈ {{convert(firstItem, secondItem, count)}}</h4>
      <b-button variant="success" @click="clearState">Clear / Effacer</b-button>
    </div>
  </div>
</template>

<script>
export default {
  name: 'UnitConverter',
  data: () => ({
    firstItem: null,
    secondItem: null,
    count: 1,
    options: [
      { value: null, text: 'unit choice' },
      { value: 'ft', text: 'Feet(s)' },
      { value: 'mi', text: 'Mile(s)' },
      { value: 'm', text: 'Meter(s)' },
      { value: 'km', text: 'Kilometer(s)' }
    ],
    unitsTable: [
      {key: 'ft', value: 0.3048},
      {key: 'mi', value: 1609.34},
      {key: 'm', value: 1},
      {key: 'km', value: 1000}
    ]
  }),
  methods: {
    convert: function(a, b, count) {
      const cf = 10;
      let meters = this.unitsTable.filter(el => el.key === a);
      if(meters[0]) {
        meters = (count * cf) * (meters[0].value * cf) / (cf * cf);
        let finalUnit = this.unitsTable.filter(el => el.key === b);
        if(finalUnit[0]) {
          finalUnit = (meters * cf) / (finalUnit[0].value * cf);
          return finalUnit;
        }
      }
      return 'Invalid data';
    },
    clearState: function() {
      this.firstItem = null;
      this.secondItem = null;
      this.count = 1;
    }
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
</style>
