"use strict";
const SwipeContainer = {
  name: "swipe-container",
  props: {},
  data() {
    return {
      isDown: false,
      startX: null,
      scrollLeft: null,
      isActive: false
    };
  },
  computed: {
    customClasses() {
      return [{ "is-active": this.isActive }];
    }
  },
  mounted() {
    this.$el.addEventListener("mousedown", this.handleMouseDown);
    this.$el.addEventListener("mouseleave", this.handleMouseLeave);
    this.$el.addEventListener("mouseup", this.handleMouseUp);
    this.$el.addEventListener("mousemove", this.handleMouseMove);
  },
  methods: {
    handleMouseDown(event) {
      this.isDown = true;
      this.isActive = true;
      this.startX = event.pageX - this.$el.offsetLeft;
      this.scrollLeft = this.$el.scrollLeft;
    },
    handleMouseLeave(event) {
      this.isDown = false;
      this.isActive = false;
    },
    handleMouseUp(event) {
      this.isDown = false;
      this.isActive = false;
    },
    handleMouseMove(event) {
      if (!this.isDown) return;
      event.preventDefault();
      const x = event.pageX - this.$el.offsetLeft;
      const distance = (x - this.startX) * 3; //scroll-fast
      this.$el.scrollLeft = this.scrollLeft - distance;
    }
  }
};

const app = new Vue({
  el: "#app",
  components: {
    SwipeContainer
  },
  data: {}
});