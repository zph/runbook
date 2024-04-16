import base64

from nbconvert.preprocessors import Preprocessor


class AddPromptPreprocessor(Preprocessor):
    """Add Prompt Preprocessor for Typescript"""

    has_import_added = False
    # TODO don't re-import a bazillion times
    import_statement = """
import { decodeBase64 } from "https://deno.land/std@0.222.1/encoding/base64.ts";
import { setTheme, printHighlight } from 'npm:@speed-highlight/core/terminal'

await setTheme('default')
const syntaxPrint = async (code: string) => {
  return await printHighlight(code, 'ts')
}

    """

    def prompt_str(self, base64Code):
        return (
            f"""
var _promptToRun = `{base64Code}`;
await syntaxPrint(new TextDecoder().decode(decodeBase64(_promptToRun)))
console.log("")
console.log("")
console.log("%cReady to run the above code?", "color: red;")
var _promptResult = prompt("Choose (y/n):");
"""
            + """
if(!_promptResult.match(/y/i)) {
  throw Error("You rejected progress")
}
console.log("")
"""
        )

    def preprocess_cell(self, cell, resources, index):
        if "source" in cell and cell.cell_type == "code":
            if type(cell.source) is str:
                s = [cell.source]
            else:
                s = cell.source

            base64code = base64.b64encode("".join(s).encode("utf-8")).decode("utf-8")
            s.insert(0, self.prompt_str(base64code))

            if not self.has_import_added:
                s.insert(0, self.import_statement)
                self.has_import_added = True

            cell.source = s
        return cell, resources
