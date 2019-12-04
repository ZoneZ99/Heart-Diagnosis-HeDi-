<template>
  <div>
    <div id="hero-header" class="grid-2">
      <div id="logo-header">
        <img src="~/assets/logo-hedi.png" alt="logo" />
        <h1>HEDI</h1>
      </div>
      <div id="content-header">
        <p>
          HEDI adalah aplikasi web yang bertujuan untuk mendiagnosis potensi penyakit jantung pada tubuh manusia. Aplikasi ini berbasis kecerdasan buatan dengan menggunakan metode Machine Learning Decision Tree. Dengan adanya aplikasi ini kami harapkan dapat membantu masyarakat di bidang kesehatan.
          <br />
          <br />
          <strong>** Aplikasi ini tidak sepenuhnya akurat. Jika terjadi gejala penyakit jantung mohon hubungi dokter untuk lebih lanjut.</strong>
        </p>
      </div>
    </div>
    <Feature />
    <Developer />
  </div>
</template>

<script>
import Developer from "@/components/developer";
import Feature from "@/components/feature";

export default {
  components: {
    Developer,
    Feature
  }
};
</script>

<style lang="scss" scoped>
div#hero-header {
  box-sizing: border-box;
  background: #f8f8f8;
  padding: 2em 4em;

  div#logo-header {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;

    h1 {
      text-transform: uppercase;
      color: #f0134d;
      font-size: 54px;
    }

    img {
      max-width: 50%;
    }
  }

  div#content-header {
    p {
      word-wrap: break-word;
      text-align: justify;
    }
  }
}

@media only screen and (min-width: 700px) {
  div#hero-header {
    display: grid;
    grid-template-columns: repeat(2, 50%);

    div#logo-header {
      img {
        width: 20%;
      }
    }

    div#content-header {
      display: flex;
      align-items: center;
    }
  }
}
</style>