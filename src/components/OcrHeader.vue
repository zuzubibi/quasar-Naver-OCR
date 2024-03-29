<template>
<div class="q-layout" view="1Hh Lpr lFf">
    <div class="q-header">
        <div class="q-px-lg q-pt-xl q-mb-md">
            <div class="text-h3">
                Subeen's OCR Check
            </div>
            <div class="text-subtitle1">{{ todaysDate }}</div>
        </div>
    </div>

</div>

</template>

<script>
import {date} from 'quasar'
export default {
    computed: {
        todaysDate (){
            const timeStamp = Date.now()
            return date.formatDate(timeStamp, 'dddd D MMMM')
        }
    }
}
</script>

<style lang="stylus" scoped>
$primary-color = #5378fb
$secondary-color = #8763fb

.q-layout
    color white
    background linear-gradient(to right, $primary-color, $secondary-color)
    padding 15px
    opacity 0.85

    .q-px-lg.q-pt-xl.q-mb-md
        .text-h3
            margin-bottom 9px
            font-weight bold

        .text-subtitle1
            font-size 17px
            font-weight bold

</style>