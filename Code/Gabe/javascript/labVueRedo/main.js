const app = new Vue({
  el: '#app',
  data: {
    result: 'Result: ',
    numberOfFeet: ''
  },
  methods: {
    converter: function() {
      this.result = 'Result: ' + (Math.round((parseInt(this.numberOfFeet) * 0.3048) * 1000) / 1000) + 'm';
      this.numberOfFeet = '';
    }
  }
})

const part2 = new Vue({
  el: '#app2',
  data: {
    amount:'',
    units: '',
    result: 'Result:'
  },
  methods: {
    convert: function() {
      if (this.units === 'in') {
        this.result = 'Result: ' + (Math.round((parseInt(this.amount) * 0.0254) * 1000) / 1000) + 'm'
        this.amount = '';
      }
      if (this.units === 'ft') {
        this.result = 'Result: ' + (Math.round((parseInt(this.amount) * 0.3048) * 1000) / 1000) + 'm'
        this.amount = '';
      }
      if (this.units === 'yd') {
        this.result = 'Result: ' + (Math.round((parseInt(this.amount) * 0.9144) * 1000) / 1000) + 'm'
        this.amount = '';
      }
      if (this.units === 'mi') {
        this.result = 'Result: ' + (Math.round((parseInt(this.amount) * 1609.34) * 1000) / 1000) + 'm'
        this.amount = '';
      }
      if (this.units === 'm') {
        this.result = 'Result: ' + (Math.round((parseInt(this.amount) * 1) * 1000) / 1000) + 'm'
        this.amount = '';
      }
      if (this.units === 'km') {
        this.result = 'Result: ' + (Math.round((parseInt(this.amount) * 1000) * 1000) / 1000) + 'm'
        this.amount = '';
      }
    }
  }
})

const part4 = new Vue({
  el: '#app3',
  data: {
    amount: '',
    startingUnits: '',
    endingUnits: '',
    result: ''
  },
  methods: {
    convert: function () {
      if (this.startingUnits === '')
    }
  }
})