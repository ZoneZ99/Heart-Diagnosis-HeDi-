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
        <a href="#">
          <li>home</li>
        </a>
        <a href="#heart-disease-danger">
          <li>heart disease</li>
        </a>
        <a href="#app-features">
          <li>Features</li>
        </a>
        <a href="#hedi-developer">
          <li>Developer</li>
        </a>
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
    padding: 1em;
    div#logo-nav {
      padding-left: 0 !important;
    }
    nav {
      display: none;
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
    padding-left: 2em;
    display: flex;
    align-items: center;

    a {
      text-decoration: none;
      display: flex;
      align-items: center;
      cursor: pointer;

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
