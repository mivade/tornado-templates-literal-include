var Test = Vue.extend({
  template: '#test-template',
  props: {
    name: String,
  }
});

new Vue({
  el: '#app',
  components: {
    test: Test
  },
  data: {
    name: ''
  }
});
