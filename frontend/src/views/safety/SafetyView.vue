<template>
  <div id="MonitoringView" class="contents-view">
    <v-container class="container-view">
      <v-row>
        <v-col>    
          <v-card
            class="mx-auto"
            min-width="100%"
          >
            <v-img
              class="white--text align-end"
              width=auto
              height="100px"
              src="../../assets/images/safety.jpg"
            >
              <v-card-title>
                <h1>Safety Monitoring</h1>
              </v-card-title>
            </v-img>
          </v-card>
        </v-col>
      </v-row>
      <v-row justify="center">
        <v-col></v-col>
        <v-col>
          <form method="post" enctype="multipart/form-data">
            <div>
              <v-file-input 
                v-model="image"
                label="사진 등록"
                prepend-icon="mdi-camera"
                @change="uploadImg()"  
              ></v-file-input>
            </div>
          </form>
          <v-card style="height:640px; width:640px;">
            <v-img :src="url"></v-img>
          </v-card>
        </v-col>
        <v-col></v-col>
      </v-row> 
      <v-row justify="center">
        <v-col></v-col>
        <v-col cols="3">
          <div>
            
            <v-btn
              class="detectbtn"
              @click="submit"
              rounded
              dark
            >
              판별하기
            </v-btn>
          </div>
        </v-col>
        <v-col></v-col>
      </v-row>
    </v-container>
  </div>
</template>

<script>
import axios from 'axios'

  export default {
    data() {
      return {
        image: null,
        url: null,
      }
    },
    methods: {
      submit(){
        let formData = new FormData();
        formData.append('image', this.image);

        axios.get('http://127.0.0.1:8000/',
          formData,
          {
            headers: {
              'Content-Type':'multipart/form-data'
            }
          }
        ).then((res) => {
          console.log(res);
        })
        .catch((err) => {
          console.log(err);
        });
      },
      // async submit() {
      //   const formData = new FormData();
      //   formData.append("image", this.image);

      //   try {
      //     const { data } = await axios.post(
      //       "http://127.0.0.1:8000/post",
      //       formData,
      //       {
      //         headers: {
      //           "Content-Type": "multipart/form-data",
      //         },
      //       }
      //     );
      // 이미지 변경 로직 넣을 것
      //     console.log(data);
      //   } catch(err) {
      //     console.log(err);
      //   }
      // },
      uploadImg() {
        this.url=URL.createObjectURL(this.image);
        console.log(this.url);
        console.log(this.image);
      },
    }
  }
</script>


<style scoped>
a{
  margin-left: 30%;
}
h1{
  margin-top: 5px;
}
.detectbtn{
  margin-left: 33%
}
</style>
  