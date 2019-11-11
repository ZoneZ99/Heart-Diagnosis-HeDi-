<template>
  <div id="form-diagnosa">
    <h1 id="title-form-diagnosa">Form Diagnosa Penyakit Jantung</h1>
    <form method="post">
      <div class="form-group">
        <label for="nama-panjang">Nama Panjang</label>
        <div>
          <input v-model="form['nama']" id="nama-panjang" type="text" />
        </div>
      </div>
      <div class="form-group">
        <label for="jenis-kelamin">Jenis Kelamin</label>
        <div>
          <select
            name="gender"
            v-model="form['jenisKelamin']"
            id="jenis-kelamin"
            aria-placeholder="Pilih Jenis Kelamin . . ."
          >
            <option value>Pilih Jenis Kelamin...</option>
            <option value="1">Laki-Laki</option>
            <option value="2">Perempuan</option>
          </select>
        </div>
      </div>
      <div class="form-group">
        <label for="tglLahir">Tanggal Lahir</label>
        <div id="tglLahir" class="row">
          <input v-model="form['tanggalLahir']" type="date" />
          <p class="format">tahun</p>
        </div>
      </div>
      <div class="form-group">
        <label for="tinggi-badan">Tinggi Badan</label>
        <div id="tinggi-badan" class="row">
          <input v-model="form['tinggiBadan']" type="text" />
          <p class="format">cm</p>
        </div>
      </div>
      <div class="form-group">
        <label for="berat-badan">Berat Badan</label>
        <div class="row">
          <input v-model="form['beratBadan']" type="text" />
          <p class="format">Kg</p>
        </div>
      </div>
      <div class="form-group">
        <label for="tekanan-sistolik">Tekanan Sistolik</label>
        <div id="tekanan-sistolik" class="row">
          <input v-model="form['tekananSistolik']" type="text" />
          <p class="format">mmHg</p>
        </div>
      </div>
      <div class="form-group">
        <label for="tingkat-kolesterol">Tingkat Kolesterol</label>
        <div id="tingkat-kolesterol" class="btn-level-group">
          <button
            type="button"
            class="btn"
            v-on:click="ColGood"
            v-bind:class="{ 'good' : isColGood }"
          >Normal (< 200)</button>
          <button
            type="button"
            class="btn"
            v-on:click="ColImportant"
            v-bind:class="{ 'good important': isColImportant }"
          >Sedang (200-239)</button>
          <button
            type="button"
            class="btn"
            v-on:click="ColDanger"
            v-bind:class="{ 'good important danger': isColDanger }"
          >Tinggi (>240)</button>
        </div>
      </div>
      <div class="form-group">
        <label for="tingkat-glukosa">Tingkat Glukosa (2 jam setelah makan)</label>
        <div id="tingkat-glukosa" class="btn-level-group">
          <button
            type="button"
            class="btn"
            v-on:click="GluGood"
            v-bind:class="{ 'good': isGluGood }"
          >Normal (< 120)</button>
          <button
            type="button"
            class="btn"
            v-on:click="GluImportant"
            v-bind:class="{ 'good important': isGluImportant }"
          >Sedang (140-199)</button>
          <button
            type="button"
            class="btn"
            v-on:click="GluDanger"
            v-bind:class="{ 'good important danger': isGluDanger }"
          >Tinggi (>200)</button>
        </div>
      </div>
      <div class="form-group">
        <input type="checkbox" v-model="form['isOlahraga']" name="olahraga" id="olahraga" />
        <label for="olahraga">Apakah kamu sering olah raga ?</label>
      </div>
      <div class="form-group">
        <input type="checkbox" v-model="form['isMerokok']" name="perokok" id="olahraga" />
        <label for="perokok">Apakah kamu seorang perokok aktif ?</label>
      </div>
      <div class="form-group">
        <input type="checkbox" v-model="form['isPeminum']" name="peminum" id="olahraga" />
        <label for="peminum">Apakah kamu seorang pecandu alkohol ?</label>
      </div>
      <div id="button-group">
        <button v-on:click="cancelForm" class="btn cancel">Batal</button>
        <button type="submit" v-on:click="submitForm" class="btn success">Diagnosa</button>
      </div>
    </form>
    <p>{{ result }}</p>
  </div>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      form: {
        nama: "",
        jenisKelamin: "",
        tanggalLahir: "",
        beratBadan: "",
        tinggiBadan: "",
        tekananSistolik: "",
        tingkatKolesterol: "normal",
        tingkatGlukosa: "normal",
        isOlahraga: false,
        isMerokok: false,
        isPeminum: false
      },
      result: "",
      isColGood: true,
      isColImportant: false,
      isColDanger: false,
      isGluGood: true,
      isGluImportant: false,
      isGluDanger: false
    };
  },
  methods: {
    submitForm() {
      event.preventDefault();
      axios
        .post("http://hedi-backend.herokuapp.com/result/", this.form)
        .then(response => {
          this.result = response.data;
        });
    },
    cancelForm() {},
    ColGood() {
      if (this.isColGood) {
        this.isColGood = true;
      } else {
        this.isColGood = !this.isColGood;
      }
      this.isColDanger = false;
      this.isColImportant = false;
      this.form.tingkatKolesterol = "normal";
    },
    ColImportant() {
      if (!this.isColGood) {
        this.isColGood = true;
      }
      if (this.isColImportant) {
        this.isColImportant = true;
      } else {
        this.isColImportant = !this.isColImportant;
      }
      this.isColDanger = false;
      this.form.tingkatKolesterol = "sedang";
    },
    ColDanger() {
      if (!this.isColImportant) {
        this.isColGood = true;
        this.isColImportant = true;
      }
      if (this.isColDanger) {
        this.isColDanger = true;
      } else {
        this.isColDanger = !this.isColDanger;
      }
      this.form.tingkatKolesterol = "tinggi";
    },
    GluGood() {
      if (this.isGluGood) {
        this.isGluGood = true;
      } else {
        this.isGluGood = !this.isGluGood;
      }
      this.isGluDanger = false;
      this.isGluImportant = false;
      this.form.tingkatGlukosa = "normal";
    },
    GluImportant() {
      if (!this.isGluGood) {
        this.isGluGood = true;
      }
      if (this.isGluImportant) {
        this.isGluImportant = true;
      } else {
        this.isGluImportant = !this.isGluImportant;
      }
      this.isGluDanger = false;
      this.form.tingkatGlukosa = "sedang";
    },
    GluDanger() {
      if (!this.isGluImportant) {
        this.isGluGood = true;
        this.isGluImportant = true;
      }
      if (this.isGluDanger) {
        this.isGluDanger = true;
      } else {
        this.isGluDanger = !this.isGluDanger;
        this.form.tingkatGlukosa = "tinggi";
      }
    }
  }
};
</script>

<style lang="scss" scoped>
div#form-diagnosa {
  h1#title-form-diagnosa {
    font-size: 32px;
    padding-bottom: 1em;
  }
}
form {
  p {
    margin: 0;
    margin-block: 0;
  }
  .form-group {
    margin-top: 20px;

    div.btn-level-group {
      display: flex;

      .btn {
        padding: 10px;
      }
    }

    div {
      margin-top: 5px;

      .btn {
        text-align: center;

        h4 {
          font-weight: 600;
        }
      }

      .good {
        background: #32dbc6;
      }

      .important {
        background: #f6d365;
      }

      .danger {
        background: #f0134d;
      }

      input {
        height: 15px;
        line-height: 15px;
      }

      input,
      select {
        background: #f8f8f8;
        padding: 5px;
        border: none;
        border-radius: 5px;
        text-overflow: ellipsis;
        overflow: hidden;
        color: #888;
        font-family: "Signika", "Arial", sans-serif;

        &:focus {
          outline: none;
          background: #eee;
        }
      }

      input.btn {
        border-radius: 0;
        height: 40px;
        padding: 10px;
      }

      p.format {
        margin-left: 10px;
      }
    }
  }
}

.row {
  display: flex;
  align-items: center;
  flex-direction: row;
}

.btn {
  outline: none;
  border: none;
  padding: 8px;
  margin: 0;
  display: block;
  color: #222;
  cursor: pointer;
  background: #eee;
}

.success {
  background: #50b6bb;
  color: white;

  &:hover {
    background: #222;
    color: white;
  }
}

.cancel {
  background: #eee;
  color: #222;

  &:hover {
    background: #222;
    color: white;
  }
}

div#button-group {
  width: 100%;
  display: flex;
  margin-top: 30px;

  .btn {
    margin-right: 10px;
    font-weight: 600;
    border-radius: 2px;
  }
}
</style>