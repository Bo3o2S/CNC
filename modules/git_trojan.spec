# -*- mode: python -*-

block_cipher = None


a = Analysis(['git_trojan.py'],
             pathex=['C:\\Users\\Bo3o2S\\Documents\\GitHub\\CNC\\modules'],
             binaries=None,
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
a.datas.append(('cacert.pem', 'cacert.pem', 'DATA'))
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='git_trojan',
          debug=False,
          strip=False,
          upx=False,
          console=False )
