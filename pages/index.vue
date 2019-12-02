<template>
  <div>
    <section id="hero-header">
      <div id="hero">
        <img id="hero-img-header" src="~/assets/hero-header.png" alt="hero-header" />
      </div>
      <div id="content-header">
        <h1 id="title-header">HEART DIAGNOSIS</h1>
        <p class="text-muted">Ayo, periksa apakah kamu memiliki gejala penyakit jantung dengan HEDI!</p>
        <nuxt-link to="formDiagnosa">
          <button>Diagnosis Sekarang !</button>
        </nuxt-link>
      </div>
    </section>

    <!-- Display Info about Heart Disease -->

    <section id="heart-disease-danger">
      <div id="content-hdd">
        <p>
          Penyakit kardiovaskular menjadi penyebab kematian nomor satu di
          Indonesia. Data dari Institute for Health Metrics and Evaluation,
          lembaga statistik kesehatan asal Amerika Serikat menyebutkan kematian
          akibat penyakit ini mencapai 36,3 persen dari total kematian di
          Indonesia pada 2016.
        </p>
      </div>
      <div id="hero-hdd">
        <img id="svg-1" src="~/assets/hero-hdd.png" alt="hero-hdd" />
      </div>
    </section>

    <!-------------------------------------->

    <!-- Display App Feature -->

    <Feature />

    <!------------------------->

    <!-- Display App Developer -->

    <Developer />

    <!--------------------------->

    <!-- Display News Related to Heart Disease -->

    <section id="news">
      <h1>Artikel Terkait</h1>
      <News />
    </section>

    <!------------------------------------------->
  </div>
</template>

<script>
import News from "@/components/news";
import Developer from "@/components/developer";
import Feature from "@/components/feature";

export default {
  components: {
    News,
    Developer,
    Feature
  }
};
</script>

<style lang="scss" scoped>
section#hero-header {
  height: 80vh;

  div#hero {
    text-align: center;

    img#hero-img-header {
      margin-top: 5vh;
      max-width: 60%;
    }
  }

  div#content-header {
    margin-top: 4em;
    text-align: right;
    padding: 0 2em;

    a {
      button {
        background: transparent;
        border: 1px solid #0c9cc3;
        padding: 8px;
        border-radius: 20px;
        font-size: 11px;
        color: #222;
        cursor: pointer;

        &:hover {
          background: #0c9cc3;
          color: white;
        }
      }
    }
  }
}

section#heart-disease-danger {
  height: 80vh;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  background: #0c9cc3;
  clip-path: polygon(0 10%, 100% 0%, 100% 90%, 0% 100%);
  padding: 2em;

  div#content-hdd {
    p {
      color: white;
      font-weight: lighter;
    }
  }

  div#hero-hdd {
    margin-top: 2em;
    text-align: center;

    img#svg-1 {
      max-width: 80%;
    }
  }
}

section#news {
  h1 {
    text-align: center;
  }
}

@media only screen and (min-width: 700px) {
  section#hero-header {
    height: 80%;
    display: grid;
    grid-template-columns: repeat(2, 50%);
    padding: 2em;

    div#content-header {
      margin-top: 0;
      display: flex;
      flex-direction: column;
      align-items: flex-end;
      justify-content: center;

      h1 {
        font-size: 5vh;
      }

      p {
        font-size: 20px;
      }
    }
  }

  section#heart-disease-danger {
    display: grid;
    grid-template-columns: repeat(2, 50%);

    div#content-hdd {
      padding: 1em;

      p {
        font-size: 18px;
      }
    }
  }
}
</style>
