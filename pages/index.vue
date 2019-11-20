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
    <section id="form-diagnosa">
      <Form />
    </section>
    <div id="news-section">
      <News />
    </div>
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
    grid-template-columns: 100% !important;

    div#content-header {
      padding: 0 2em 4em 2em !important;
    }
  }
}

div#hero-header {
  display: grid;
  grid-template-columns: repeat(2, 50%);
  box-sizing: border-box;

  div#hero {
    display: flex;
    margin-top: 2em;
    margin-left: -8em;
    width: 100%;
    img {
      max-height: 60vh;
      max-width: 100vw;
    }
  }

  div#content-header {
    display: flex;
    flex-direction: column;
    align-items: flex-end;
    justify-content: center;
    padding: 0 4em 0 6em;

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