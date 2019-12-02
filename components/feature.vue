<template>
  <div>
    <section id="app-features">
      <h1>What you get from Hedi...</h1>
      <div class="container">
        <div class="card-container">
          <div class="card">
            <img src="~/assets/machine-learning.png" alt="img-feature" />
            <h1>Machine Learning</h1>
            <p>
              Hedi menerapkan metode
              <i>Decision Tree</i> untuk mengolah
              data-datanya.
            </p>
          </div>
        </div>
        <div class="card-container">
          <div class="card">
            <img src="~/assets/accuracy.png" alt="img-feature" />
            <h1>Accuracy</h1>
            <p>
              Tingkat akurasi Hedi cukup meyakinkan. Tree dibuat dengan tingkat
              akurasi sebesar
              <strong>76%</strong>.
            </p>
          </div>
        </div>
        <div class="card-container">
          <div class="card">
            <img src="~/assets/machine-learning.png" alt="img-feature" />
            <h1>User Friendly</h1>
            <p>
              Aplikasi Hedi sangat mudah digunakan. Pengguna hanya perlu mengisi
              form yang berisi informasi terkait kesehatan mereka.
            </p>
          </div>
        </div>
      </div>
    </section>
  </div>
</template>

<script>
export default {};
</script>

<style lang="scss" scoped>
section#app-features {
  h1 {
    padding: 2em;
    font-size: 24px;
  }

  div.container {
    width: 100%;
    box-sizing: border-box;
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));

    div.card-container {
      display: flex;
      align-items: center;
      justify-content: center;

      div.card {
        width: 200px;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        margin: 1em;
        padding: 2em;
        box-shadow: 5px 0px 20px #eee;

        h1 {
          text-align: center;
          padding: 20px;
          margin: 0;
        }

        img {
          max-width: 200px;
        }

        p {
          text-align: center;
          font-weight: lighter;
        }
      }
    }
  }
}

@media only screen and (min-width: 700px) {
  section#app-features {
    padding: 4em;
    h1 {
      font-size: 4vh;
    }

    div.container {
      width: 100%;
      div.card-container {
        div.card {
          h1 {
            text-align: center;
            padding: 20px;
            margin: 0;
          }
        }
      }
    }
  }
}
</style>