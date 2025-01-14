# kiss-gfx

Packaged some gfx-related builds!

:pencil2: **Image editor:**
`gimp` `grafx2`

:black_nib: **Vector graphics editor:**
`inkscape`

## kiss-hooks

In order to build `gimp`, we need to set this hooks:

```shell
case $TYPE in
    pre-build)
        case $PKG in
            atk)
                sed -i "s/-Dintrospection=false/-Dintrospection=true/g"       "$repo_dir/build"
            ;;
            gdk-pixbuf)
                sed -i "s/-Dgir=false/-Dgir=true/g"                           "$repo_dir/build"
            ;;
            gtk+3)
                sed -i "s/-introspection=no/-introspection=yes/g"             "$repo_dir/build"
                sed -i 's/rm/#rm/g'                                           "$repo_dir/build"
            ;;
            pango)
                sed -i "s/-Dintrospection=disabled/-Dintrospection=enabled/g" "$repo_dir/build"
                sed -i "s/-Dgir=false/-Dgir=true/g"                           "$repo_dir/build"
            ;;
        esac
    ;;
    post-build)
        case $PKG in
            atk)
                sed -i "s/-Dintrospection=true/-Dintrospection=false/g"       "$repo_dir/build"
            ;;
            gdk-pixbuf)
                sed -i "s/-Dgir=true/-Dgir=false/g"                           "$repo_dir/build"
            ;;
            gtk+3)
                sed -i "s/-introspection=yes/-introspection=no/g"             "$repo_dir/build"
                sed -i 's/#rm/rm/g'                                           "$repo_dir/build"
            ;;
            pango)
                sed -i "s/-Dintrospection=enabled/-Dintrospection=disabled/g" "$repo_dir/build"
                sed -i "s/-Dgir=true/-Dgir=false/g"                           "$repo_dir/build"
            ;;
        esac
    ;;
esac
```

In order to build `inkscape`, we need to set this hooks:

```shell
case $TYPE in
    pre-build)
        case $PKG in
            atk|pango)
                sed -i "s/-Dintrospection=false/-Dintrospection=true/g" "$repo_dir/build"
            ;;
            gdk-pixbuf|pango)
                sed -i "s/-Dgir=false/-Dgir=true/g"                     "$repo_dir/build"
            ;;
            gtk+3)
                sed -i "s/-introspection=no/-introspection=yes/g"       "$repo_dir/build"
            ;;
            poppler)
                _flags=-DENABLE_UNSTABLE_API_ABI_HEADERS=ON

                sed -i "s/-DENABLE_CPP=ON/$_flags \0/"                  "$repo_dir/build"
            ;;
        esac
    ;;
    post-build)
        case $PKG in
            atk|pango)
                sed -i "s/-Dintrospection=true/-Dintrospection=false/g" "$repo_dir/build"
            ;;
            gdk-pixbuf|pango)
                sed -i "s/-Dgir=true/-Dgir=false/g"                     "$repo_dir/build"
            ;;
            gtk+3)
                sed -i "s/-introspection=yes/-introspection=no/g"       "$repo_dir/build"
            ;;
            poppler)
                _flags=-DENABLE_UNSTABLE_API_ABI_HEADERS=ON

                sed -i "s/$_flags //"                                   "$repo_dir/build"
            ;;
        esac
    ;;
esac
```
