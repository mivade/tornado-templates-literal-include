var Test = Vue.extend({
  template: '#test-template',
  props: {
    name: String,
  }
});

var SecondTest = Vue.extend({
  template: '#test2-template',
  props: {
    name: String
  }
});

new Vue({
  el: '#first',
  components: {
    test: Test
  },
  data: {
    name: ''
  }
});

new Vue({
  el: '#second',
  components: {
    test: SecondTest
  },
  data: {
    name: 'Ben'
  }
});
