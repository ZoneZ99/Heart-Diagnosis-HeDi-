<template>
  <div>
    <div id="hero-header">
      <div id="hero">
        <img src="~/assets/hero-header.png" alt="hero-header">
      </div>
      <div id="content-header">
        <p>Penyakit kardiovaskular menjadi penyebab kematian nomor satu di Indonesia. Data dari Institute for Health Metrics and Evaluation, lembaga statistik kesehatan asal Amerika Serikat menyebutkan kematian akibat penyakit ini mencapai 36,3 persen dari total kematian di Indonesia pada 2016.</p>
        <p>
          <strong>Ayo, periksa apakah kamu memiliki gejala penyakit jantung dengan HEDI !</strong>
        </p>
        <a href="#title-form-diagnosa">
          <button>Diagnosis Sekarang !</button>
        </a>
      </div>
    </div>
    <div id="news-section">
      <News />
    </div>
    <section id="form-diagnosa">
      <Form />
    </section>
  </div>
</template>

<script>
import Form from "@/components/form";
import News from "@/components/news";

export default {
  components: {
    Form,
    News
  }
};
</script>

<style lang="scss" scoped>
@media only screen and (max-width: 700px) {
  div#hero-header {
    height: 85vh !important;
    div#hero {
      top: 5vh !important;
      left: -30vw !important;
      img {
        max-width: 80% !important;
      }
    }
  }

  div#content-header {
    position: absolute;
    top: 45vh !important;
    width: 80% !important;
  }
}

div#hero-header {
  position: relative;
  box-sizing: border-box;
  height: 70vh;

  div#hero {
    position: absolute;
    top: 5vh;
    left: -8vw;
    z-index: -1;

    img {
      background-size: cover;
      max-height: 80vh;
      max-width: 50vw;
    }

  }

  div#content-header {
    float: right;
    margin: 5em;
    display: flex;
    flex-direction: column;
    align-items: flex-end;
    justify-content: center;
    width: 30%;

    p {
      word-wrap: break-word;
      text-align: justify;
    }

    button {
      cursor: pointer;
      background: #f0134d;
      color: white;
      border-radius: 5px;
      border: none;
      padding: 8px;
      font-weight: bold;

      &:hover {
        background: #222;
      }
    }
  }
}

section#form-diagnosa {
  display: flex;
  justify-content: center;
  align-items: center;
}

div#news-section {
  display: flex;
  align-items: center;
  justify-content: center;
}
</style>