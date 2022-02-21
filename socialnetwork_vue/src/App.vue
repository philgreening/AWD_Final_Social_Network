<template>
  <div id="wrapper">
      <nav class="navbar navbar-dark bg-dark">
        <div class="container-fluid">
          <div class="navbar-brand">
            <router-link to="/" class="navbar-brand"><strong>Social Network</strong></router-link>
          </div>
          <ul class="navbar-nav me-auto mb-2 mb-lg-0">
            <li class="nav-item">
              <router-link to="/feed" class="nav-link"><strong>Feed</strong></router-link>
            </li>

            <li class="nav-item">
              <router-link to="/log-in" class="btn btn-light"><strong>Log In</strong></router-link>
            </li>
          </ul>
        </div>
      </nav>
    <router-view/>
  </div>
</template>

<style lang="scss">
@import '../node_modules/bootstrap'
</style>
