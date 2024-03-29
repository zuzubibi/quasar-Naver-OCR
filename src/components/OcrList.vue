<template>
    <div class="imgClass">
        <img :src="img" alt="사진">
        <ul>
            <li v-for="(infoItem, index) in value" :key="index">
                <div class="mini">{{ infoItem.key }}</div>
                {{ infoItem.value }}
            </li>
        </ul>
    </div>
</template>

<script>
    export default {
        props: ['value'],
        data(){
            return {
                // imgData: "https://storage.googleapis.com/cdn-asia/ocr/S25C-923071315520.jpg",
                img: require("../img/IMG_5505.jpeg"),
            }
        },
        computed:{
            settingData(){
                console.log(this.value);
                return this.value
            }
        }       
    }
</script>

<style lang="stylus" scoped>
.imgClass
    width 100%
    height 100%
    // background red
    img
        width 400px
    ul
        list-style-type none
        padding-left 0px
        margin-top 20px
        text-align left

    li
        display flex
        min-height 50px
        height 50px
        line-height 50px
        margin 0.5rem 30px
        padding 0 0.9rem
        background white
        border-radius 5px
        .mini
            font-weight bold
            margin-right 20px

</style>