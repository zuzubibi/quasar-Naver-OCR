<template>
  <div id="q-app">
    <ocr-header></ocr-header>
    <ocr-input-photo @input="getData"></ocr-input-photo>
    <ocr-list v-model="data"></ocr-list>
    <ocr-footer></ocr-footer>
  </div>
</template>

<script>
import OcrHeader from './components/OcrHeader.vue';
import OcrInputPhoto from './components/OcrInputPhoto.vue';
import OcrList from './components/OcrList.vue';
import OcrFooter from './components/OcrFooter.vue';

export default {
  data() {
    return {
      data: []
    }
  },
  components: { 
    OcrHeader, 
    OcrInputPhoto, 
    OcrList, 
    OcrFooter 
  },
  methods:{
    getData(info){
      this.data = info;
    }
  }
}
</script> 

<style>
body {
  text-align: center;
  background-color: #f6f6f6
}
input {
  border-style: groove;
  width: 200px;
}
button{
  border-style: groove;
}
.shadow{
  box-shadow: 5px 10px 10px rgba(0,0,0, 0.03);
}
</style>