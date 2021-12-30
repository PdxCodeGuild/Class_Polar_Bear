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
    result: '',
    conversions: {
      in: 1/ 0.02540,
      ft: 1/0.3048,
      yd: 1/0.91440,
      mi: 1/1609.34,
      m: 1,
      km: 1/1000
    }
  },
  methods: {
    convert: function () {
      let tempNum = 0;
      if (this.startingUnits === 'in') {
        tempNum = (Math.round((parseInt(this.amount) * 0.0254) * 1000) / 1000) * this.conversions[this.endingUnits]
        this.amount = '';
      }
      if (this.startingUnits === 'ft') {
        tempNum = (Math.round((parseInt(this.amount) * 0.3048) * 1000) / 1000) * this.conversions[this.endingUnits]
        this.amount = '';
      }
      if (this.startingUnits === 'yd') {
        tempNum = (Math.round((parseInt(this.amount) * 0.9144) * 1000) / 1000) * this.conversions[this.endingUnits]
        this.amount = '';
      }
      if (this.startingUnits === 'mi') {
        tempNum = (Math.round((parseInt(this.amount) * 1609.34) * 1000) / 1000) * this.conversions[this.endingUnits]
        this.amount = '';
      }
      if (this.startingUnits === 'm') {
        tempNum = (Math.round((parseInt(this.amount) * 1) * 1000) / 1000) * this.conversions[this.endingUnits]
        this.amount = '';
      }
      if (this.startingUnits === 'km') {
        tempNum = (Math.round((parseInt(this.amount) * 1000) * 1000) / 1000) * this.conversions[this.endingUnits]
        this.amount = '';
      }
      this.result = tempNum;
    }
  }
})