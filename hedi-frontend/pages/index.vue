<template>
  <div>
    <Nav />
    <section id="hero-header">
      <div id="hero" data-aos="fade-up">
        <img
          id="hero-img-header"
          src="~/assets/hero-header.png"
          alt="hero-header"
        />
      </div>
      <div id="content-header" data-aos="fade-left">
        <h1 id="title-header">HEART DIAGNOSIS</h1>
        <p class="text-muted">
          Ayo, periksa apakah kamu memiliki gejala penyakit jantung dengan HEDI!
        </p>
        <nuxt-link to="formDiagnosa">
          <button>Diagnosis Sekarang !</button>
        </nuxt-link>
      </div>
    </section>
    <!-- Display Info about Heart Disease -->

    <section id="heart-disease-danger" data-aos="fade-up">
      <div id="content-hdd" data-aos="fade-right">
        <p>
          Menurut WHO, penyakit kardiovaskular adalah penyebab nomor 1 kematian
          secara global. Diperkirakan 17,9 juta orang meninggal karena penyakit
          kardiovaskular pada tahun 2016, angka ini mewakili 31% dari semua
          kematian global. Dari kematian ini, 85% disebabkan oleh serangan
          jantung dan stroke. Di Indonesia penyakit kardiovaskular dikaitkan
          dengan penyakit jantung. Penyakit kardiovaskular dapat meliputi
          kondisi tertentu yang melibatkan jantung dan pembuluh darah.
        </p>
      </div>
      <div id="hero-hdd" data-aos="fade-left">
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

    <News />

    <!------------------------------------------->
  </div>
</template>

<script>
import Nav from "../layouts/partials/Nav";
import News from "@/components/news";
import Developer from "@/components/developer";
import Feature from "@/components/feature";
import AOS from "aos";

export default {
  scrollToTop: true,
  components: {
    Nav,
    News,
    Developer,
    Feature
  },
  mounted() {
    AOS.init();
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
  height: 100vh;
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

@media only screen and (min-width: 700px) {
  section#hero-header {
    height: 92vh;
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
    height: 100vh;
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
