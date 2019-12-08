<template>
  <div id="form-diagnosa">
    <transition name="fade">
      <div class="errorMessage" v-if="showError == true">
        <p>{{ error }}</p>
      </div>
    </transition>
    <transition name="fade">
      <div class="modal center" v-if="showResult == true">
        <div class="overlay"></div>
        <div id="result" v-bind:class="[ {greenGradient : !isCancer}, {redGradient : isCancer}]">
          <i class="material-icons">close</i>
          <div class="center">
            <p id="description">
              Hasil diagnosa menunjukkan bahwa
              <br />
              <span>{{ form.nama }}</span>
            </p>
            <h1 v-if="result === 1">Terindikasi</h1>
            <h1 v-else-if="result === 0">Tidak Terindikasi</h1>
            <p>Penyakit Jantung</p>
          </div>
        </div>
      </div>
    </transition>
    <client-only>
      <full-page ref="fullpage" :options="options" id="fullpage">
        <div class="section">
          <div class="center">
            <div class="form-group">
              <label for="namaPanjang">Siapa nama kamu ? *</label>
              <div>
                <input
                  placeholder="Tulis nama kamu disini..."
                  v-model="form['nama']"
                  id="namaPanjang"
                  type="text"
                  class="input-text"
                  v-on:keyup.enter="nextInput"
                />
              </div>
              <div class="flex">
                <button class="btn out-green" v-on:click="nextInput">Oke</button>
              </div>
              <p class="scroll">
                <i class="material-icons">arrow_downward</i> Scroll ke bawah
                untuk melanjutkan !
              </p>
            </div>
          </div>
        </div>

        <div class="section">
          <div class="center">
            <div class="form-group">
              <label for="jenisKelamin">Jenis Kelamin Kamu,____? *</label>
              <div>
                <select
                  name="gender"
                  v-model="form['jenisKelamin']"
                  id="jenisKelamin"
                  aria-placeholder="Pilih Jenis Kelamin . . ."
                  class="input-text"
                  v-on:keyup.enter="nextInput"
                >
                  <option value>Pilih Jenis Kelamin...</option>
                  <option value="1">Perempuan</option>
                  <option value="2">Laki-Laki</option>
                </select>
              </div>
              <div class="flex">
                <button class="btn" v-on:click="prevInput">Balik</button>
                <button class="btn out-green" v-on:click="nextInput">Oke</button>
              </div>
              <p class="scroll">
                <i class="material-icons">arrow_downward</i> Scroll ke bawah
                untuk melanjutkan !
              </p>
            </div>
          </div>
        </div>

        <div class="section">
          <div class="center">
            <div class="form-group">
              <label for="tglLahir">Tanggal Lahir</label>
              <div class="row">
                <input
                  id="tglLahir"
                  v-model="form['tanggalLahir']"
                  type="date"
                  class="input-text"
                  v-on:keyup.enter="nextInput"
                />
                <p class="format">tahun</p>
              </div>
              <div class="flex">
                <button class="btn" v-on:click="prevInput">Balik</button>
                <button class="btn out-green" v-on:click="nextInput">Oke</button>
              </div>
              <p class="scroll">
                <i class="material-icons">arrow_downward</i> Scroll ke bawah
                untuk melanjutkan !
              </p>
            </div>
          </div>
        </div>

        <div class="section">
          <div class="center">
            <div class="form-group">
              <label for="tinggiBadan">Tinggi Badan</label>
              <div class="row">
                <input
                  id="tinggiBadan"
                  v-model="form['tinggiBadan']"
                  type="number"
                  min="0"
                  class="input-number"
                  v-on:keyup.enter="nextInput"
                />
                <p class="format">cm</p>
              </div>
              <div class="flex">
                <button class="btn" v-on:click="prevInput">Balik</button>
                <button class="btn out-green" v-on:click="nextInput">Oke</button>
              </div>
              <p class="scroll">
                <i class="material-icons">arrow_downward</i> Scroll ke bawah
                untuk melanjutkan !
              </p>
            </div>
          </div>
        </div>

        <div class="section">
          <div class="center">
            <div class="form-group">
              <label for="berat-badan">Berat Badan</label>
              <div class="row">
                <input
                  id="beratBadan"
                  v-model="form['beratBadan']"
                  type="number"
                  min="0"
                  class="input-number"
                  v-on:keyup.enter="nextInput"
                />
                <p class="format">Kg</p>
              </div>
              <div class="flex">
                <button class="btn" v-on:click="prevInput">Balik</button>
                <button class="btn out-green" v-on:click="nextInput">Oke</button>
              </div>
              <p class="scroll">
                <i class="material-icons">arrow_downward</i> Scroll ke bawah
                untuk melanjutkan !
              </p>
            </div>
          </div>
        </div>

        <div class="section">
          <div class="center">
            <div class="form-group">
              <label for="tekananSistolik">Tekanan Sistolik</label>
              <div class="row">
                <input
                  id="tekananSistolik"
                  v-model="form['tekananSistolik']"
                  type="number"
                  min="0"
                  class="input-number"
                  v-on:keyup.enter="nextInput"
                />
                <p class="format">mmHg</p>
              </div>
              <div class="flex">
                <button class="btn" v-on:click="prevInput">Balik</button>
                <button class="btn out-green" v-on:click="nextInput">Oke</button>
              </div>
              <p class="scroll">
                <i class="material-icons">arrow_downward</i> Scroll ke bawah
                untuk melanjutkan !
              </p>
            </div>
          </div>
        </div>

        <div class="section">
          <div class="center">
            <div class="form-group">
              <label for="tekananSistolik">Tekanan Diastolik</label>
              <div class="row">
                <input
                  id="tekananDiastolik"
                  v-model="form['tekananDiastolik']"
                  type="number"
                  min="0"
                  class="input-number"
                  v-on:keyup.enter="nextInput"
                />
                <p class="format">mmHg</p>
              </div>
              <div class="flex">
                <button class="btn" v-on:click="prevInput">Balik</button>
                <button class="btn out-green" v-on:click="nextInput">Oke</button>
              </div>
              <p class="scroll">
                <i class="material-icons">arrow_downward</i> Scroll ke bawah
                untuk melanjutkan !
              </p>
            </div>
          </div>
        </div>

        <div class="section" v-on:keyup.enter="nextInput">
          <div class="center">
            <div class="form-group">
              <label for="tingkat-kolesterol">Tingkat Kolesterol</label>
              <div id="tingkat-kolesterol" class="btn-level-group">
                <button
                  type="button"
                  class="btn option"
                  v-on:click="ColGood"
                  v-bind:class="{ good: isColGood }"
                >Normal (< 200)</button>
                <button
                  type="button"
                  class="btn option"
                  v-on:click="ColImportant"
                  v-bind:class="{ 'good important': isColImportant }"
                >Sedang (200-239)</button>
                <button
                  type="button option"
                  class="btn option"
                  v-on:click="ColDanger"
                  v-bind:class="{ 'good important danger': isColDanger }"
                >Tinggi (>240)</button>
              </div>
              <div class="flex">
                <button class="btn" v-on:click="prevInput">Balik</button>
                <button class="btn out-green" v-on:click="nextInput">Oke</button>
              </div>
              <p class="scroll">
                <i class="material-icons">arrow_downward</i> Scroll ke bawah
                untuk melanjutkan !
              </p>
            </div>
          </div>
        </div>

        <div class="section" v-on:keyup.enter="nextInput">
          <div class="center">
            <div class="form-group">
              <label for="tingkat-glukosa">Tingkat Glukosa (2 jam setelah makan)</label>
              <div id="tingkat-glukosa" class="btn-level-group">
                <button
                  type="button"
                  class="btn option"
                  v-on:click="GluGood"
                  v-bind:class="{ good: isGluGood }"
                >Normal (< 120)</button>
                <button
                  type="button"
                  class="btn option"
                  v-on:click="GluImportant"
                  v-bind:class="{ 'good important': isGluImportant }"
                >Sedang (140-199)</button>
                <button
                  type="button"
                  class="btn option"
                  v-on:click="GluDanger"
                  v-bind:class="{ 'good important danger': isGluDanger }"
                >Tinggi (>200)</button>
              </div>
              <div class="flex">
                <button class="btn" v-on:click="prevInput">Balik</button>
                <button class="btn out-green" v-on:click="nextInput">Oke</button>
              </div>
              <p class="scroll">
                <i class="material-icons">arrow_downward</i> Scroll ke bawah
                untuk melanjutkan !
              </p>
            </div>
          </div>
        </div>

        <div class="section" v-on:keyup.enter="nextInput">
          <div class="center">
            <div class="form-group">
              <input type="checkbox" v-model="form['isOlahraga']" name="olahraga" id="olahraga" />
              <label for="olahraga">Apakah kamu sering olah raga ?</label>
              <div class="flex">
                <button class="btn" v-on:click="prevInput">Balik</button>
                <button class="btn out-green" v-on:click="nextInput">Oke</button>
              </div>
            </div>

            <p class="scroll">
              <i class="material-icons">arrow_downward</i> Scroll ke bawah
              untuk melanjutkan !
            </p>
          </div>
        </div>

        <div class="section" v-on:keyup.enter="nextInput">
          <div class="center">
            <div class="form-group">
              <input type="checkbox" v-model="form['isMerokok']" name="perokok" id="perokok" />
              <label for="perokok">Apakah kamu seorang perokok aktif ?</label>
              <div class="flex">
                <button class="btn" v-on:click="prevInput">Balik</button>
                <button class="btn out-green" v-on:click="nextInput">Oke</button>
              </div>
            </div>
            <p class="scroll">
              <i class="material-icons">arrow_downward</i> Scroll ke bawah
              untuk melanjutkan !
            </p>
          </div>
        </div>

        <div class="section" v-on:keyup.enter="nextInput">
          <div class="center">
            <div class="form-group">
              <input type="checkbox" v-model="form['isPeminum']" name="peminum" id="peminum" />
              <label for="peminum">Apakah kamu seorang pecandu alkohol ?</label>
              <div class="flex">
                <button class="btn" v-on:click="prevInput">Balik</button>
                <button class="btn out-green" v-on:click="nextInput">Oke</button>
              </div>
            </div>
            <p class="scroll">
              <i class="material-icons">arrow_downward</i> Scroll ke bawah
              untuk melanjutkan !
            </p>
          </div>
        </div>

        <div class="section">
          <div class="center">
            <div class="form-group">
              <label>Diagnosa Sekarang ?</label>
              <div class="flex">
                <button class="btn" v-on:click="prevInput">Balik</button>
                <button type="submit" v-on:click="submitForm" class="btn success">Diagnosa</button>
              </div>
            </div>
          </div>
        </div>
      </full-page>
    </client-only>
  </div>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      options: {
        licenseKey: "YOUR_KEY_HERE"
      },
      form: {
        nama: "",
        jenisKelamin: "",
        tanggalLahir: "",
        beratBadan: 0,
        tinggiBadan: 0,
        tekananSistolik: 0,
        tekananDiastolik: 0,
        tingkatKolesterol: 1,
        tingkatGlukosa: 1,
        isOlahraga: false,
        isMerokok: false,
        isPeminum: false
      },
      showResult: false,
      result: "",
      isCancer: false,
      isColGood: true,
      isColImportant: false,
      isColDanger: false,
      isGluGood: true,
      isGluImportant: false,
      isGluDanger: false,
      showError: false,
      error: "",
      loading: false
    };
  },
  methods: {
    prevInput() {
      fullpage_api.moveSectionUp();
    },
    nextInput() {
      fullpage_api.moveSectionDown();
    },
    submitForm() {
      event.preventDefault();

      this.loading = true;
      if (this.form.nama == "") {
        this.showError = true;
        this.error = "Isi Nama terlebih dahulu !";
        fullpage_api.moveTo(1);
        setTimeout(this.hideError, 3000);
      } else if (this.form.jenisKelamin == "") {
        this.showError = true;
        this.error = "Isi Jenis Kelamin terlebih dahulu !";
        fullpage_api.moveTo(2);
        setTimeout(this.hideError, 3000);
      } else if (this.form.tanggalLahir == "") {
        this.showError = true;
        this.error = "Isi Tanggal Lahir terlebih dahulu !";
        fullpage_api.moveTo(3);
        setTimeout(this.hideError, 3000);
      } else if (this.form.beratBadan == 0) {
        this.showError = true;
        this.error = "Isi Berat Badan dengan benar !";
        fullpage_api.moveTo(4);
        setTimeout(this.hideError, 3000);
      } else if (this.form.tinggiBadan == 0) {
        this.showError = true;
        this.error = "Isi Tinggi Badan dengan benar !";
        fullpage_api.moveTo(5);
        setTimeout(this.hideError, 3000);
      } else {
        axios
          .post("https://hedi-backend.herokuapp.com/result/", this.form)
          .then(response => {
            this.result = response.data.result;
            if (result === 1) isCancer = true;
            else isCancer = false;
            this.showResult = true;
          });
      }
    },
    hideResult() {
      this.showResult = false;
    },
    hideError() {
      this.showError = false;
    },
    ColGood() {
      if (this.isColGood) {
        this.isColGood = true;
      } else {
        this.isColGood = !this.isColGood;
      }
      this.isColDanger = false;
      this.isColImportant = false;
      this.form.tingkatKolesterol = 1;
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
      this.form.tingkatKolesterol = 2;
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
      this.form.tingkatKolesterol = 3;
    },
    GluGood() {
      if (this.isGluGood) {
        this.isGluGood = true;
      } else {
        this.isGluGood = !this.isGluGood;
      }
      this.isGluDanger = false;
      this.isGluImportant = false;
      this.form.tingkatGlukosa = 1;
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
      this.form.tingkatGlukosa = 2;
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
        this.form.tingkatGlukosa = 3;
      }
    }
  }
};
</script>

<style lang="scss" scoped>
@media only screen and (max-width: 700px) {
  div#form-diagnosa {
    .section {
      padding: 2em !important;

      .scroll {
        font-size: 14px;

        .material-icons {
          font-size: 18px;
        }
      }

      .form-group {
        label {
          font-size: 16px;
        }

        p.format {
          font-size: 18px;
        }

        input,
        select {
          font-size: 16px;
        }

        .input-text {
          width: 75%;
          height: 2em;
        }
        .input-number {
          width: 75%;
          height: 2em;
        }
      }
    }
  }
}
div#form-diagnosa {
  h1#title-form-diagnosa {
    font-size: 32px;
    padding-bottom: 1em;
  }

  .section {
    height: 100vh;
    width: 100vw;
    padding: 0 10em;

    .center {
      display: flex;
      flex-direction: column;
      align-items: flex-start;
      justify-content: center;
    }
  }

  p.scroll {
    margin-top: 25px;
    font-weight: lighter;

    i {
      animation: UpDown 1s infinite;
    }
  }

  .form-group {
    width: 100%;

    .input-text {
      width: 100%;
      height: 3em;
    }

    .input-number {
      width: 100%;
      height: 3em;
    }

    div.btn-level-group {
      display: flex;

      .btn {
        padding: 10px;
      }
    }

    label {
      font-size: 24px;
      font-weight: bold;
    }

    div {
      margin-top: 10px;
      .btn {
        text-align: center;

        h4 {
          font-weight: 600;
        }
      }

      input {
        height: 15px;
        line-height: 15px;
      }

      input,
      select {
        background: transparent;
        border: none;
        border-bottom: 1px solid #eee;
        text-overflow: ellipsis;
        overflow: hidden;
        color: #888;
        font-size: 24px;
        font-family: "Signika", "Arial", sans-serif;
        transition: all 0.5s ease;

        &:focus {
          outline: none;
          border-bottom: 1px solid black;
        }
      }

      input.btn {
        border-radius: 0;
        height: 40px;
        padding: 10px;
      }

      p {
        margin-top: 0;
        margin-bottom: 0;
      }

      p.format {
        margin-left: 10px;
        font-size: 24px;
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
  margin: 0 5px 0 0;
  display: block;
  color: #222;
  cursor: pointer;
  background: #eee;

  &.good {
    background: #32dbc6;
  }

  &.important {
    background: #f6d365;
  }

  &.danger {
    background: #f0134d;
  }

  &.out-green {
    background: transparent;
    border: 1px solid #32dbc6;

    &:hover {
      background: #32dbc6;
    }
  }

  &.option {
    border-radius: 0;
    margin: 0;
  }

  &:hover {
    background: #222;
    color: #eee;
  }
}

h1 {
  .good {
    color: #32dbc6;
  }

  .bad {
    color: #f0134d;
  }
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

a {
  text-decoration: none;
}

.v-flex-center {
  display: flex;
  align-items: center;
  justify-content: center;
}

.errorMessage {
  position: fixed;
  top: 0;
  left: 50%;
  z-index: 1;
  background: #f0134d;
  transform: translateX(-50%);
  width: 100%;
  color: #eee;
  font-weight: lighter;
  font-size: 16px;
  text-align: center;
  animation: slideDown 0.5 ease;
}

.modal {
  position: absolute;
  z-index: 2;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  height: 100%;
  width: 100%;

  .overlay {
    width: 100%;
    height: 100%;
    background: #222;
    opacity: 0.2;
    position: absolute;
  }

  &.center,
  .center {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    text-align: center;
  }

  .greenGradient {
    background: linear-gradient(45deg, rgb(21, 211, 163), rgb(117, 218, 231));
    color: white;
  }

  .redGradient {
    background: linear-gradient(45deg, rgb(211, 59, 21), rgb(231, 140, 117));
    color: white;
  }

  #result {
    z-index: 2;
    border-radius: 20px;
    margin: 2em;
    padding: 1em;
    text-align: right;

    i {
      font-size: 16px;
      cursor: pointer;

      &:hover {
        transform: scale(1.2);
      }
    }
  }
}

div.flex {
  display: flex;
}

.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.5s;
}
.fade-enter, .fade-leave-to /* .fade-leave-active below version 2.1.8 */ {
  opacity: 0;
}

/* Safari 4.0 - 8.0 */
@-webkit-keyframes UpDown {
  0% {
    transform: translateY(0px);
  }
  50% {
    transform: translateY(4px);
  }
  100% {
    transform: translateY(0px);
  }
}

/* Standard syntax */
@keyframes UpDown {
  0% {
    transform: translateY(0px);
  }
  50% {
    transform: translateY(4px);
  }
  100% {
    transform: translateY(0px);
  }
}
</style>
