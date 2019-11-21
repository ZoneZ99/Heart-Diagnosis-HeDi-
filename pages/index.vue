<template>
  <div>
    <section id="hero-header">
      <div id="hero">
        <img id="hero-img-header" src="~/assets/hero-header.png" alt="hero-header" />
        <img id="bg-img-header" src="~/assets/bg-header.png" alt="bg-header" />
      </div>
      <div id="content-header">
        <h1 id="title-header">HEART DIAGNOSIS</h1>
        <p class="text-muted">Ayo, periksa apakah kamu memiliki gejala penyakit jantung dengan HEDI!</p>
        <a href="#title-form-diagnosa">
          <button>Diagnosis Sekarang !</button>
        </a>
      </div>
    </section>
    <section id="heart-disease-danger">
      <div id="content-hdd">
        <p>
          <strong>Penyakit kardiovaskular</strong> menjadi penyebab kematian nomor satu di Indonesia. Data dari Institute for Health Metrics and Evaluation, lembaga statistik kesehatan asal Amerika Serikat menyebutkan kematian akibat penyakit ini mencapai 36,3 persen dari total kematian di Indonesia pada 2016.
        </p>
      </div>
      <div id="hero-hdd">
        <img id="svg-1" src="~/assets/svg-1.png" alt="hero-hdd" />
      </div>
    </section>
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
@media only screen and (max-width: 800px) {
  section#hero-header {
    grid-template-columns: 100% !important;

    div#content-header {
      padding: 0 2em 4em 4em !important;
    }
  }

  section#heart-disease-danger {
    grid-template-columns: 100% !important;

    div#hero-hdd {
      img {
        top: 120vh !important;
        max-height: 50% !important;
      }
    }
  }
}

section#heart-disease-danger {
  height: 100vh;
  display: grid;
  grid-template-columns: repeat(2, 50%);

  div#content-hdd {
    height: 100%;
    padding-left: 4em;
    padding-right: 2em;
    display: flex;
    flex-direction: column;
    justify-content: center;

    p {
      font-size: 24px;
    }
  }

  div#hero-hdd {
    img {
      max-height: 80%;
    }

    img#svg-1 {
      position: absolute;
      z-index: -1;
      top: 80vh;
      right: -10vw;
    }
  }
}

section#hero-header {
  display: grid;
  grid-template-columns: repeat(2, 50%);
  box-sizing: border-box;

  div#hero {
    display: flex;
    padding-top: 2em;
    margin-left: -4em;
    width: 100%;

    img#hero-img-header {
      max-height: 65vh;
      max-width: 100vw;
    }

    img#bg-img-header {
      position: absolute;
      max-height: 90%;
      max-width: 100%;
      top: 0;
      left: 0;
      z-index: -1;
    }
  }

  div#content-header {
    display: flex;
    flex-direction: column;
    align-items: flex-end;
    justify-content: center;
    padding: 0 4em 0 6em;
    text-align: right;

    h1 {
      font-size: 54px;
    }

    p {
      word-wrap: break-word;
    }

    .text-muted {
      font-weight: 300;
      color: #aaa;
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