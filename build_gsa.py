import os
import shutil
import subprocess


class FileReader:
    """Baca file dan bersihkan dari komentar dan baris kosong."""

    @staticmethod
    def read_and_clean(path: str) -> str:
        if not os.path.exists(path):
            raise FileNotFoundError(f"File not found: {path}")

        cleaned_lines = []
        with open(path, "r", encoding="utf-8") as f:
            for line in f:
                stripped = line.strip()
                # skip baris kosong dan komentar XML
                if not stripped or stripped.startswith("<!--"):
                    continue
                cleaned_lines.append(stripped)

        return "\n".join(cleaned_lines)


class TemplateProcessor:
    """Menyisipkan konten lighting ke placeholder template XML."""

    def __init__(
        self,
        template_path: str,
        placeholder: str = "<!-- INSERT_LIGHTS_HERE -->",
    ):
        self.template_path = template_path
        self.placeholder = placeholder

    def inject_content(self, content: str) -> str:
        if not os.path.exists(self.template_path):
            raise FileNotFoundError(
                f"Template tidak ditemukan: {self.template_path}"
            )

        with open(self.template_path, "r", encoding="utf-8") as f:
            template = f.read()

        if self.placeholder not in template:
            raise ValueError(
                f"Placeholder '{self.placeholder}' tidak ditemukan di template."
            )

        return template.replace(self.placeholder, content)


class FileWriter:
    """Tulis hasil build dan salin ke direktori game."""

    @staticmethod
    def write_output(output_path: str, content: str):
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"[✔] File berhasil dibuat: {output_path}")

    @staticmethod
    def copy_to_game(src: str, dest_folder: str):
        if not os.path.exists(src):
            raise FileNotFoundError(f"File output tidak ditemukan: {src}")
        if not os.path.exists(dest_folder):
            raise FileNotFoundError(
                f"Folder tujuan tidak ditemukan: {dest_folder}"
            )

        shutil.copy2(src, dest_folder)
        print(f"[✔] File disalin ke: {dest_folder}")


class Compiler:
    """Menjalankan compile_gsa.bat jika diaktifkan."""

    @staticmethod
    def run(batch_path: str):
        if not os.path.exists(batch_path):
            raise FileNotFoundError(f"File batch tidak ditemukan: {batch_path}")
        print("[⏳] Menjalankan compile_gsa.bat ...")
        subprocess.run([batch_path], shell=True, check=True)
        print("[✔] Selesai menjalankan compile_gsa.bat")


class GSABuilder:
    """Main class untuk menjalankan semua tahap build."""

    def __init__(
        self,
        source_xml: str,
        template_xml: str,
        output_xml: str,
        game_graphics_dir: str,
        batch_path: str = None,
        run_compile: bool = False,
    ):
        self.source_xml = source_xml
        self.template_xml = template_xml
        self.output_xml = output_xml
        self.game_graphics_dir = game_graphics_dir
        self.batch_path = batch_path
        self.run_compile = run_compile

    def build(self):
        print("[1] Membaca dan membersihkan source XML...")
        source_content = FileReader.read_and_clean(self.source_xml)

        print("[2] Menyisipkan ke template...")
        processor = TemplateProcessor(self.template_xml)
        final_content = processor.inject_content(source_content)

        print("[3] Menulis hasil build...")
        FileWriter.write_output(self.output_xml, final_content)

        print("[4] Menyalin hasil ke direktori game...")
        FileWriter.copy_to_game(self.output_xml, self.game_graphics_dir)

        if self.run_compile and self.batch_path:
            print("[5] Menjalankan compile_gsa.bat...")
            Compiler.run(self.batch_path)

        print("[✔] Proses build selesai!")


def main():
    builder = GSABuilder(
        source_xml="Graphics/floor2.source.xml",
        template_xml="Graphics/1-percent-better.template.xml",
        output_xml="_build/Graphics/gsa_info.xml",
        game_graphics_dir="D:/Games/Bully Scholarship Edition/Graphics/",
        batch_path="D:/Games/Bully Scholarship Edition/Graphics/compile_gsa.bat",
        run_compile=True,  # ubah ke False jika tidak ingin auto compile
    )
    builder.build()


if __name__ == "__main__":
    main()
