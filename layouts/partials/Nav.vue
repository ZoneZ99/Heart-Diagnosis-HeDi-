<template>
  <header>
    <div id="logo-nav">
      <nuxt-link id="title-nav" to="/">hedi</nuxt-link>
    </div>
    <nav>
      <ul>
        <nuxt-link to="/">
          <li>home</li>
        </nuxt-link>
        <nuxt-link to="/about">
          <li>about</li>
        </nuxt-link>
      </ul>
    </nav>
  </header>
</template>

<script>
export default {};
</script>

<style scoped lang="scss">
header {
  position: sticky;
  top: 0;
  box-sizing: border-box;
  display: grid;
  grid-template-columns: repeat(2, 50%);
  background: white;
  box-shadow: 10px 0.1px 10px #ddd;

  div#logo-nav {
    display: flex;
    align-items: center;
    padding-left: 2em;

    a {
      text-decoration: none;
      color: #f0134d;
      font-size: 24px;
      font-weight: bold;
      text-transform: uppercase;
    }
  }

  nav {
    padding-right: 2em;

    ul {
      display: flex;
      justify-content: flex-end;
      align-items: center;

      a {
        text-decoration: none;
        color: #2b2b28;
        padding: 1em 2em;
        text-transform: uppercase;

        li {
          list-style: none;
        }

        &:hover {
          text-shadow: 0 0 1px #222;
        }
      }
    }
  }
}
</style>