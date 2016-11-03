fornever.me: Engineer, Programmer, Gentleman [![Status Ventis](https://img.shields.io/badge/status-ventis-yellow.svg)](https://github.com/ForNeVeR/andivionian-status-classifier) [![Build status](https://ci.appveyor.com/api/projects/status/dh7qx27hrjs8chp3/branch/develop?svg=true)](https://ci.appveyor.com/project/ForNeVeR/fornever-me/branch/develop)
============================================

This is the [fornever.me][] site source code. It uses ForneverMind — a simple
homemade blog engine mainly written in F# programming language.

Build
-----

### Frontend

To compile frontend part, you'll need a recent (6.9.1+) [Node.js][node-js]
installation and [Yarn package manager][yarn] (version 0.16.1+). Then execute
the following script inside of the `ForneverMind.Frontend` directory:

```console
$ yarn install
$ yarn run webpack # or `yarn run optimize` for optimized build
```

_(You may alternatively use Webpack-compatible task runner for your IDE.)_

You don't have to install yarn globally. Here's an instruction how to install it
locally for the project (from the solution root directory):

```console
$ npm install yarn@0.16.1
$ cd ForneverMind.Frontend
$ ../node_modules/.bin/yarn install
$ ../node_modules/.bin/yarn run optimize
```

### Backend

To compile the backend, you'll need [NuGet][nuget] and [MSBuild][msbuild] or a
compatible build engine.

Here's a simple build script:

```console
$ nuget restore
$ msbuild /p:Platform="Any CPU" /p:Configuration=Release ForneverMind.sln
```

There's an MSBuild property `/p:DeployBackend=true` that will deploy the site to
the directory configured in `ForneverMind/__profiles/Production.pubxml`.

Other components
----------------

1.  [EvilPlanner][evil-planner] meant to be an integral part of the site, but it
    need to be installed separately.
2.  [fornever.me][] uses an easy-to-install [Disqus][disqus] comment system.

[disqus]: https://disqus.com/
[evil-planner]: https://github.com/ForNeVeR/EvilPlanner
[fornever.me]: https://fornever.me/
[msbuild]: https://msdn.microsoft.com/en-us/library/dd393574.aspx
[node-js]: https://nodejs.org/
[nuget]: https://www.nuget.org/
[yarn]: https://yarnpkg.com/
