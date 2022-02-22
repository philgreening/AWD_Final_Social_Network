<template>
  <div id="wrapper">
    <nav class="navbar navbar-expand navbar-dark bg-dark">
      <div class="container-fluid">
        <router-link to="/" class="navbar-brand"><strong>Social Network</strong></router-link>
        <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navcollapse" aria-controls="navcollapse" aria-expanded="false" aria-label="Toggle navigation">
          <span class="navbar-toggler-icon"></span>
        </button>
        
      <div class="collapse navbar-collapse" id="navcollapse">
        <ul class="navbar-nav mr-auto">
          <li class="nav-item ">
            <router-link to="/feed" class="nav-link"><strong>Feed</strong></router-link>
          </li>
        </ul>
        <router-link to="/log-in" class="btn btn-light"><strong>Log In</strong></router-link>
        </div>
      </div>
    </nav>
    <router-view/>
  </div>
</template>

<style lang="scss">
@import '../node_modules/bootstrap'
</style>
