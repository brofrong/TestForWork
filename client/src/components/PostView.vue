<template>
    <v-container 
        fill-height
        fluid
    >
        <v-row
            justify="center"
            >
            <v-col
                align="center"
            >
                <Card
                    v-bind="cardData"
                />
                <v-row
                    justify="center"
                >
                    <v-btn
                        elevation="5"
                        class="ma-4"
                        height="75"
                        width="75"
                        icon
                        @click="likeDislike(false)"
                    >
                        <v-icon
                            class="mt-1"
                            size=50
                            color=red
                        >
                            mdi-close
                        </v-icon>
                    </v-btn>
                    <v-btn
                        elevation="5"
                        class="ma-4"
                        height="75"
                        width="75"
                        @click="likeDislike(true)"
                        icon
                    >
                        <v-icon
                            class="mt-1"
                            size=50
                            color=green
                        >
                            mdi-heart
                        </v-icon>
                    </v-btn>
                </v-row>
            </v-col>
        </v-row>

    </v-container>
</template>

<script>

import Card from './Card';

export default {
    components:{
        Card
    },
    data: () =>{
        return{
            cardData:{
                name: "",
                imgsrc:"",
                aboutlanguage:"",
                tags:"",
                likes:"0",
                dislikes:"0"
            },
            posts:'',
            postNumber:0
        }
    },
    methods:{
        loadCard(){
            var post = this.posts[this.postNumber]
            this.cardData.name = post[1]
            this.cardData.imgsrc = post[2]
            this.cardData.aboutlanguage = post[3]
            this.cardData.tags = post[4].split(',')
            this.cardData.likes = post[5]
            this.cardData.dislikes = post[6]
       },
       likeDislike(islike){
           var postID = this.posts[this.postNumber][0]
           if(islike){
               this.posts[this.postNumber][5]++
               this.cardData.likes++
               this.$axios
                    .get(this.$hostname + "/like?id="+postID)
                    .then(() => {this.nextCard()})
                    .catch(error => console.log(error))
           }
           else{
               this.posts[this.postNumber][6]++
               this.cardData.dislikes++
               this.$axios
                    .get(this.$hostname + "/dislike?id="+postID)
                    .then(() => {this.nextCard()})
                    .catch(error => console.log(error))
           }
       },
       nextCard(){
           this.postNumber++
           if(this.postNumber>=this.posts.length){
               this.postNumber=0
           }
           this.loadCard()
       }
    },
    mounted(){
        this.$axios
            .get(this.$hostname + "/getposts")
            .then(response => {this.posts = response.data; this.loadCard()})
            .catch(error => console.log(error))
    }

}
</script>

<style>

</style>