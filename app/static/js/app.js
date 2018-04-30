/* Add your Application JavaScript */
Vue.component('app-header', {
    template: `
        
            <nav class="navbar navbar-expand-lg navbar-dark bg-primary fixed-top">
              <span><img src="/static/uploads/pic.png" alt="home page picture" style="width:20px;height:20px;"/>
              <a class="navbar-brand" href="#">Photogram</a></span>
              <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
                <span class="navbar-toggler-icon"></span>
              </button>
              
              
              <div class="collapse navbar-collapse " id="navbarNav">
                <ul class="navbar-nav mr-auto">
                
                </ul>
                <ul class="navbar-nav">
                     <li class="nav-item active">
                        <router-link to="/" class="nav-link">Home</router-link>
                     </li>
                     <li class="nav-item active">
                         <router-link to="/explore" class="nav-link">Explore</router-link>
                     </li>
                     <li class="nav-item active">
                           <router-link to="/users/{users_id}" class="nav-link">My Profile</router-link>
                     </li>
                     <li v-if="msg=='yes'" class="nav-item active">
                           <router-link to="/logout" class="nav-link">Logout</router-link>
                     </li>
                     <li v-else class="nav-item active">
                        <router-link to="/login" class="nav-link">Login</router-link> 
                     </li>
                </ul>
              </div>
            </nav>
        
    `
});

Vue.component('app-footer', {
    template: `
        <footer>
            <div class="container">
                <p>Copyright &copy {{ year }} Flask Inc.</p>
            </div>
        </footer>
    `,
    data: function() {
        return {
            year: (new Date).getFullYear()
        }
    }
});

const Home = Vue.component('home', {
        template: `
         <div class="Frame">
          <div class="homePic">
          <img src="/static/uploads/download.jpg" alt="home page picture" style="width:400px;height:400px;"/>
          </div>
          
           <div class="Welcome">
           <div class="padtext">
             <h1><img src="/static/uploads/pic.jpg" alt="home page picture" style="width:20px;height:20px;"/> Photogram</h1>
            </div>
            <div class="pad">
             <p> Share photos of your favourite moments with friends, family and the world.</p> 
            </div>
            <div>
             <router-link class="btn btn-success col-md-5" to="/register">Register</router-link>
            <router-link class="btn btn-primary col-md-5" to="/login">Login</router-link>
            </div>
           </div>
        </div>
         `
    });

const Register=Vue.component('register',{
     template:`
     <div>
        <div v-if='messageFlag' >
        
            <div v-if="!errorFlag ">
                <div class="alert alert-success" >
                    {{ message }}
                </div>
            </div>
            <div v-else >
                <ul class="alert alert-danger">
                    <li v-for="error in message">
                        {{ error }}
                    </li>
                </ul>
            </div>
            
        </div>
     <div>
     <h1 class="b">Register </h1>
     
     <form class="form" id="register" @submit.prevent="Register" method="POST" enctype="multipart/form-data">
                 
        <div>
            <label>Firstname:</label><br/>
            
           <input type='text' id='firstname' name='firstname' style="width: 100%;"/>
        </div>
        <div>
            <label>Lastname:</label><br/>
           <input type='text' id='lastname' name='lastname' style="width: 100%;"/>
        </div>
        <div>
            <label>Username:</label><br/>
           <input type='text' id='username' name='username' style="width: 100%;"/>
           
        </div>
        <div>
            <label>Password:</label><br/>
           <input type='password' id='password' name='password' style="width: 100%;"/>
        </div>
        <div>
            <label>Email:</label><br/>
           <input type='text' id='email' name='email' placeholder="shaquillemartin@example.com" style="width: 100%;"/>
        </div>
        <div>
            <label>Location:</label><br/>
           <input type='text' id='location' name='location' style="width: 100%;"/>
        </div>
        <div>
            <label>Biography:</label><br/>
           <textarea name="biography"> </textarea><br/>
        </div>
        <div>
            <label for='profile_photo' class='btn btn-primary'>Browse....</label> <span>{{ filename }}</span>
            
            <input id="photo" type="file" name='photo' style="display: none" v-on:change = "onFileSelected" /><br/>
            
            <input type="submit" value="Upload" class="btn btn-success"/>
        </div>
            
             <div>
                  <button id="submit" class="btn btn-success">Sign Up</button> 
                </div>
            
        </form>
     </div> `,
     methods:{
        Register : function(){
            let self = this
            let registerForm= document.getElementById('register');
            let form_data = new FormData(register);
    
            fetch("/api/users/register",{
                method:'POST',
                body: form_data,
                headers:{
                    'X-CSRFToken':token
                },
                credentials: 'same-origin'
            })
              .then(function(response){
                  return response.json();
              })
              .then(function(jsonResponse){
                  //display a success message
                  console.log(jsonResponse);
              })
              .catch(function(error){
                  console.log(error);
              });
        }
    }
});

const Login=Vue.component('login',{
     template:`
     <div class="Frame">
     <h1 class="b">Login</h1>
     <form class="form" id="login" @submit.prevent="LoginForm" method="POST" >
         <div>
         <label for="username">Username</label><br>
         <input type='text' name='username'/>
         </div>
         <div>
         <label for="password">Password</label><br>
         <input type='password' name='password'/>
         </div>
         <br>
         <input type="checkbox" name="remember me" value="true" class="c"/>Remember me <br>
         <button type="submit" class="btn btn-primary greenbut butsize1">Login</button>
     </form>
     </div>
     `,
     methods:{
        LoginForm: function(){
            let loginForm= document.getElementById('login');
            let form_data = new FormData(loginForm);
    
            fetch("/api/auth/login",{
                method:'POST',
                body: form_data,
                headers:{
                    'X-CSRFToken':token
                },
                credentials: 'same-origin'
            })
              .then(function(response){
                  return response.json();
              })
              .then(function(jsonResponse){
                  //display a success message
                  console.log(jsonResponse);
              })
              .catch(function(error){
                  console.log(error);
              });
        }
    }
    
});
    
const Logout = Vue.component("logout", {
  created: function(){
    const self = this;
    
    fetch("api/auth/logout", {
      method: "POST",
      headers: {
        "Authorization": `Bearer ${localStorage.token}`
      },
      credentials: "same-origin"
    }).then(function(response){
      return response.json();
    }).then(function(jsonResponse){
      localStorage.removeItem("token");
      router.go();
      router.push("/");
    }).catch(function(error){
      console.log(error);
    });
  }
});
    
const Explore=Vue.component('explore',{
  template:`
            <div v-if="usertoken !=''">
                <div style="margin-top: 20%;">
                    <router-link class="btn btn-success col-md-5" to="/postnew">New Post</router-link>
                </div>
                <div v-if="posts.length>=1">
                    <div v-for="post in posts">
                        <img style="width:100px; height:100px" v-bind:src="post.userphoto"><h4>{{post.username}}</h4>
                        <img style="width:600px; height:600px" v-bind:src="post.photo"/>
                        <p>{{post.caption}}</p>
                        <div>
                            <div v-if="post.likebyuser=='No'">
                                <button :id=post.id v-on:click="like(post.id)" style="background-color:transparent">
                                    <img style="width:35px; height:35px" v-bind:src="'static/uploads/pgheart.png'" />
                                </button>
                            </div>
                            <div v-else>
                                <button style="background-color:transparent" disabled>
                                    <img style="width:35px; height:35px" v-bind:src="'static/uploads/pgheart.png'" />
                                </button>
                            </div>
                        <p>Likes: <span :id="'like'+post.id">{{post.likes}}</span></p></div>
                        <p>{{post.created_on}}</p>
                    </div>
                </div>
                <div v-else>
                    <h5> No Posts</h5>
                </div>
        </div>
        <div v-else>
            <h3>You are not Logged in</h3>
        </div>`,
        created: function () {
            let self = this;
            if(localStorage.getItem('token')!==null){
                self.usertoken=localStorage.getItem('token');
                console.log(self.usertoken);
                fetch("/api/posts", { 
                method: 'GET',
                headers: {
                        'Authorization': 'Bearer ' + localStorage.getItem('token'),
                        'X-CSRFToken': token
                    },
                credentials: 'same-origin'
                
                })
                .then(function (response) {
                    return response.json();
                })
                .then(function (jsonResponse) {
        
                    self.posts=jsonResponse.response['0']['posts'];
                    console.log(self.posts);
                })
                .catch(function (error) {
                    console.log(error);
                });
            }
        },
        data:function(){
            return {
                response:[],
                posts:[],
                error:[],
                usertoken:''
            }
        },
        methods:{
            like:function(postid){
                let self= this;
                let likevalue=document.getElementById('like'+postid).innerHTML;
                likevalue=parseInt(likevalue)+1;
                fetch("/api/posts/"+postid+"/like", { 
                    method: 'POST',
                    headers: {
                            'Authorization': 'Bearer ' + localStorage.getItem('token'),
                            'X-CSRFToken': token
                        },
                    credentials: 'same-origin'
                    
                    })
                    .then(function (response) {
                        return response.json();
                    })
                    .then(function (jsonResponse) {
                        if (jsonResponse.response){
                            alert(jsonResponse.response['0']['message']);
                            document.getElementById('like'+postid).innerHTML=likevalue;
                            document.getElementById(postid).disabled=true;
                        }
                    })
                    .catch(function (error) {
                        console.log(error);
                    });
            }
                
        }
})

    
const UserPost=Vue.component('Userposts',{
template:`<div v-if="usertoken!==''">
                <div v-if="error ===''">
                    <div>
                        <img style="width:100; height:100px;" v-bind:src="userinfo.photo" />
                        <p>{{userinfo.fname}}<span> {{userinfo.lname}}</span></p>
                        <p>{{userinfo.location}}</p>
                        <p>{{userinfo.joined}}</p>
                        <p>{{userinfo.bio}}</p>
                    </div>
                    <div>
                        <p>{{numposts}} </br> Posts</p>
                        <p><span id='followers'>{{follows}}</span> </br>Following</p>
                        <div v-if="toshow=='Yes'">
                            <form method="POST" @submit.prevent="follow">
                                <input  id='userid' type="hidden" :value=userinfo.id >
                                <button id='follow'>Follow</button>
                            </form>
                        </div>
                        <div v-if="isfollowing !==''">
                            <p>{{isfollowing}}</p>
                        </div>
                    </div>
                    <div v-if="posts.length > 0">
                        <div v-for="photo in posts">
                            <img v-bind:src="photo.photo"/>
                        </div>
                    </div>
                    <div v-else><h3>No posts yet</h3></div>
                </div>
                <div v-else><h1>User Doesn't exist</h1></div>
            </div>
            <div v-else>
                <h3>You are not logged in</h3>
            </div>`,
        created: function () {
            if(localStorage.getItem('token')!==null){
                let self = this;
                self.usertoken=localStorage.getItem('token');
                fetch("/api/users/"+this.$route.params.user_id+"/posts", { 
                method: 'GET',
                headers: {
                        'Authorization': 'Bearer ' + localStorage.getItem('token'),
                        'X-CSRFToken': token
                    },
                credentials: 'same-origin'
                
                })
                .then(function (response) {
                    return response.json();
                })
                .then(function (jsonResponse) {
                    if (jsonResponse.response){
                        self.posts=jsonResponse.response['0']['posts']['0'];
                        self.numposts=jsonResponse.response['0']['numposts'];
                        self.follows=jsonResponse.response['0']['follows'];
                        self.userinfo=jsonResponse.response['0']['userinfo'];
                        console.log(self.userinfo);
                        if((jsonResponse.response['0']['current']==='No' &&  jsonResponse.response['0']['following']==='No')===true){
                            self.toshow='Yes';
                        }
                        if(jsonResponse.response['0']['current']==='No' && jsonResponse.response['0']['following']==='Yes'){
                                self.isfollowing='You are already following '+self.userinfo['username'];
                        }
                    }
                    else{
                        self.error=jsonResponse.error['error'];
                    }
                })
                .catch(function (error) {
                    console.log(error);
                });
            }
            
        },
        data:function(){
            return {
                usertoken:'',
                posts:[],
                follows:0,
                numposts:0,
                userinfo:[],
                isfollowing:'',
                error:'',
                toshow:'',
            }
        },methods:{
            follow:function(){
                let self= this;
                let followid=document.getElementById('userid').value;
                let updatefollows=document.getElementById('followers').innerHTML;
                updatefollows=parseInt(updatefollows)+1;
                fetch("/api/users/"+followid+"/follow", { 
                    method: 'POST',
                    headers: {
                            'Authorization': 'Bearer ' + localStorage.getItem('token'),
                            'X-CSRFToken': token
                        },
                    credentials: 'same-origin'
                    
                    })
                    .then(function (response) {
                        return response.json();
                    })
                    .then(function (jsonResponse) {
                        if (jsonResponse.response){
                            alert(jsonResponse.response['message']);
                            document.getElementById('followers').innerHTML=updatefollows;
                            document.getElementById('follow').disabled=true;
                        }
                    })
                    .catch(function (error) {
                        console.log(error);
                    });
            }
                
        }
})
    
const Post=Vue.component('post',{
     template:` 
      <div>
      <form class="form" id="post" @submit.prevent="PostForm method="POST" enctype="multipart/form-data" >
         <div>
              <div>
              <label for="msg">Photo</label><br>
              <input type="file" name="photo" />
              </div>
              
              <label for="Caption">Caption</label><br>
              <textarea id="Caption" name="Caption" placeholder="Write Caption"></textarea>
             </div>
             <br>
             <button type="submit" class="btn btn-primary greenbut butsize1">Submit</button>
      </form>
      </div>
     `,
     methods:{
        PostForm: function(){
            let postForm= document.getElementById('post');
            let form_data = new FormData(postForm);
    
            fetch("/api/users/{user_id}/posts",{
                method:'POST',
                body: form_data,
                headers:{
                    'X-CSRFToken':token
                },
                credentials: 'same-origin'
            })
              .then(function(response){
                  return response.json();
              })
              .then(function(jsonResponse){
                  //display a success message
                  console.log(jsonResponse);
              })
              .catch(function(error){
                  console.log(error);
              });
        }
    }
    });
   
const router = new VueRouter({
         routes: [
         { path: '/', component: Home },
         { path: '/register', component: Register},
         { path: '/explore', component: Explore},
         { path: '/login' , component: Login}, 
         { path: '/logout', component: Logout},
         { path: '/users/{user_id}', component: UserPost},
         { path: '/post/new', component: Post}
         ]
    });


//Root Instance
let app = new Vue({
    el: '#app',
    router
});