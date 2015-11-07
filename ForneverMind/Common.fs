﻿module ForneverMind.Common

open System.IO

open Arachne.Http
open Freya.Core
open Freya.Machine
open Freya.Machine.Extensions.Http

let private utf8 = Freya.init [ Charset.Utf8 ]
let private json = Freya.init [ MediaType.Html ]

let get = Freya.init [ GET ]

let machine =
    freyaMachine {
        using http
        charsetsSupported utf8
        mediaTypesSupported json
    }

let pathIsInsideDirectory directory path =
    let fullDirectory = Path.GetFullPath directory
    let fullPath = Path.GetFullPath path
    fullPath.StartsWith fullDirectory
