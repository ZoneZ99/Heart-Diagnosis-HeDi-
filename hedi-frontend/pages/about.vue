<template>
  <div>
    <div id="hero-header" class="grid-2">
      <div id="logo-header">
        <h1>hedi</h1>
      </div>
      <div id="content-header">
        <p>
          HEDI adalah aplikasi web yang bertujuan untuk mendiagnosis potensi penyakit jantung pada tubuh manusia. Aplikasi ini berbasis kecerdasan buatan dengan menggunakan metode Machine Learning Decision Tree. Dengan adanya aplikasi ini kami harapkan dapat membantu masyarakat di bidang kesehatan.
          <br />
          <br />Note : Aplikasi ini tidak sepenuhnya akurat. Jika terjadi gejala penyakit jantung mohon hubungi dokter untuk lebih lanjut.
        </p>
      </div>
    </div>
    <section id="hedi-developer">
      <h1>Men Behind The Project</h1>
      <div class="grid">
        <div class="card">
          <div class="circle"></div>
          <h3 class="name">Ahmad Supriyanto</h3>
          <p class="description">Frontend Developer</p>
        </div>
        <div class="card">
          <div class="circle"></div>
          <h3 class="name">Alfian Fuadi</h3>
          <p class="description">Programmer</p>
        </div>
        <div class="card">
          <div class="circle"></div>
          <h3 class="name">Farhan Azyumardhi</h3>
          <p class="description">Programmer</p>
        </div>
        <div class="card">
          <div class="circle"></div>
          <h3 class="name">Vincentius Adi</h3>
          <p class="description">Programmer</p>
        </div>
      </div>
    </section>
  </div>
</template>

<script>
export default {};
</script>

<style lang="scss" scoped>
@media only screen and (max-width: 800px) {
  div#hero-header {
    padding: 2em !important;
    display: grid;
    grid-template-columns: 100% !important;

    div#logo-header {
      display: flex;
      align-items: center !important;
      justify-content: center !important;
      margin-right: 0 !important;
    }
  }
}

section#hedi-developer {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  padding: 4em;

  .grid {
    margin-top: 2em;
    width: 100%;
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));

    .card {
      padding: 2em;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;

      .circle {
        height: 8em;
        width: 8em;
        background: #eee;
        clip-path: circle(50% at 50% 50%);
        margin-bottom: 2em;
        z-index: -1;
      }

      p {
        margin-block: 0;
        text-align: center;
      }

      h3 {
        text-align: center;
      }
    }
  }
}

div#hero-header {
  box-sizing: border-box;
  background: #f8f8f8;
  padding: 2em 4em;
  display: grid;
  grid-template-columns: 25% 75%;

  div#logo-header {
    display: flex;
    align-items: center;
    justify-content: flex-end;
    margin-right: 2em;

    h1 {
      text-transform: uppercase;
      color: #f0134d;
      font-size: 54px;
    }
  }

  div#content-header {
    p {
      word-wrap: break-word;
      text-align: justify;
    }
  }
}
</style>