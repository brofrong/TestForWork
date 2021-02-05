<template>
  <v-app>
    <AppBar v-on:change='() => {creatingpost = !creatingpost}'/>
    <v-main>
      <CreatePost v-if="creatingpost"/>
      <PostView v-else hidden=true /> 
    </v-main>
  </v-app>
</template>

<script>
import PostView from './components/PostView';
import CreatePost from './components/CreatePost';
import AppBar from './components/AppBar'
 
export default {
  name: 'App',

  components: {
    PostView,
    CreatePost,
    AppBar
  },
  data: () => {
    return{
      creatingpost: false
    }
  },
};
</script>
