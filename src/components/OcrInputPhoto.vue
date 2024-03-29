<template>
    <div class="ex">
        <q-btn class="editBtn" push label="click me" @click="sendPhoto"/>

        
    </div>
</template>

<script>
import { OcrData } from '../api/index'

export default {
    data(){
        return {
            // 주민등록증
            photo:'https://storage.googleapis.com/cdn-asia/ocr/IMG_5505.jpeg',
            info: [],
        }
    },
    methods: {
        async sendPhoto(){
            const UserData = {
                url: this.photo
            }
            const { data } = await OcrData(UserData);
            this.info = data;
            this.$emit('input', this.info);
        }
    }
}
</script>

<style lang="stylus" scoped>
$primary-color = #5378fb
$secondary-color = #8763fb

.ex
    display block
    justify-content center
    align-items center
    width 100%
    height 100%
    // background red

    .editBtn
        margin 50px 0px
        font-size 14px
        border-radius 10px
        background linear-gradient(to right, $primary-color, $secondary-color)
        color white
        margin-right 4px

</style>