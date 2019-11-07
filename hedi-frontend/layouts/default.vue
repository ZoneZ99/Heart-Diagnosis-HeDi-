<template>
  <div>
    <Nav />
    <nuxt />
  </div>
</template>

<script>
import Nav from "./partials/Nav";

export default {
  components: {
    Nav
  }
};
</script>

<style lang="scss">
html {
  scroll-behavior: smooth;
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
