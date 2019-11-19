<template>
  <div>
    <div id="hero-header" class="grid-2">
      <div id="logo-header">
        <h1>hedi</h1>
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
  </div>
</template>

<script>
import Form from "@/components/form";

export default {
  components: {
    Form
  }
};
</script>

<style lang="scss" scoped>
@media only screen and (max-width: 800px) {
  div#hero-header {
    padding: 2em !important;
    display: grid;
    grid-template-columns: 100% !important;

    div#logo-header {
      margin-top: 0 !important;
      margin-right: 0 !important;
      display: flex;
      align-items: center !important;
      justify-content: center !important;
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
    align-items: flex-start;
    justify-content: flex-end;
    margin-top: 1.5em;
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
</style>