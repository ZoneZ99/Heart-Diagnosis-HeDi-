<template>
  <div>
    <Nav />
    <nuxt />
    <Footer />
  </div>
</template>

<script>
import Nav from "./partials/Nav";
import Footer from "./partials/Footer";

export default {
  components: {
    Nav,
    Footer
  }
};
</script>

<style lang="scss">
html {
  scroll-behavior: smooth;
}
* {
  box-sizing: border-box;
}
section {
  overflow: hidden;
}
html,
body,
h1,
h2,
h3,
h4 {
  margin: 0;
  font-family: "Signika", sans-serif;
}
</style>
