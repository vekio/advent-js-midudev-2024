{
  description = "advent-js-midudev-2024";

  inputs.nixpkgs.url = "https://flakehub.com/f/NixOS/nixpkgs/0.1.*.tar.gz";

  outputs = { self, nixpkgs }:
    let

      supportedSystems =
        [ "x86_64-linux" "aarch64-linux" "x86_64-darwin" "aarch64-darwin" ];

      forEachSupportedSystem = f:
        nixpkgs.lib.genAttrs supportedSystems
        (system: f { pkgs = import nixpkgs { inherit system; }; });
    in {
      devShells = forEachSupportedSystem ({ pkgs }: {
        default = pkgs.mkShell {
          name = "advent-js-midudev-2024";

          venvDir = ".venv";
          packages = with pkgs;
            [ python311 ]
            ++ (with pkgs.python311Packages; [ pip venvShellHook ]);
          env = { };

          shellHook = "";
        };
      });
    };
}
