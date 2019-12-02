<template>
  <header>
    <div id="logo-nav">
      <nuxt-link id="title-nav" to="/">
        <img id="logo" src="~/assets/logo-hedi.png" alt="logo" />
        <span>Hedi</span>
      </nuxt-link>
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
@media only screen and (max-width: 800px) {
  header {
    nav {
      ul {
        a {
          padding: 10px !important;
        }
      }
    }
  }
}

header {
  position: sticky;
  top: 0;
  left: 0;
  right: 0;
  z-index: 1;
  box-sizing: border-box;
  display: grid;
  grid-template-columns: 25% 75%;
  background: rgba($color: #fff, $alpha: 0.8);

  div#logo-nav {
    display: flex;
    align-items: center;
    padding-left: 2em;

    a {
      text-decoration: none;
      display: flex;
      align-items: center;

      span {
        color: #f0134d;
        font-size: 16px;
        font-weight: bold;
        text-transform: uppercase;
        margin-left: 5px;
      }

      img#logo {
        max-width: 24px;
      }
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